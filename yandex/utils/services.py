import requests
from bs4 import BeautifulSoup
from yandex.utils.setting import SettingRequest
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from yandex.models import YandexInformation, YandexReview, YandexCompanyData


def get_yandex_company_data(organization_slug, organization_id):
    try:
        url = SettingRequest.get_url(organization_slug, organization_id)

        headers = SettingRequest.headers.value

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response = response.text
            soup = BeautifulSoup(response, "html.parser")
            meta_block = soup.find('div', class_='business-summary-rating-badge-view')

            rating_raw = meta_block.find('div', class_='business-summary-rating-badge-view__rating').text
            average_rating = float(rating_raw.split('\xa0')[1].replace(',', '.'))

            reviews_count_raw = meta_block.find('span', class_='business-rating-amount-view').text
            reviews_count = int(reviews_count_raw.split()[0])

            return {'average_rating': average_rating, 'reviews_count': reviews_count}

        return {'average_rating': None, 'reviews_count': None}
    except Exception:
        return {'average_rating': None, 'reviews_count': None}


def get_yandex_reviews_data(
        organization_slug: str,
        organization_id: str,
):
    """
    Параметры:
    organization_slug (str): Слаг компании на Яндекс Картах. Пример: "naparili_dv"
    organization_id (str): ID компании на Яндекс Картах. Пример: 68956168702
    limit (int): Максимальное количество отзывов
    min_rating (int): Минимальная оценка отзыва

    Возвращает:
    list[dict], float, int: Возвращает список отзывов, средний рейтинг компании и общее количество отзывов
    """
    try:
        url = SettingRequest.get_url(organization_slug, organization_id)

        headers = SettingRequest.headers.value

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response = response.text
            soup = BeautifulSoup(response, "html.parser")

            review_blocks = soup.findAll('div', class_='business-reviews-card-view__review')
            reviews = []
            for review_block in review_blocks:
                author = review_block.find('div', class_='business-review-view__author-name').find('span').text
                text = review_block.find('span', class_='business-review-view__body-text').text
                stars = len(review_block.find('div', class_='business-rating-badge-view__stars').findAll('span', class_='_full'))

                created_at_str = review_block.find('span', class_='business-review-view__date').find('span').text

                author_avatar = review_block.find('div', class_='user-icon-view__icon').get('style')
                if author_avatar:
                    author_avatar = author_avatar.split('url(')[1][:-1]

                photos_blocks = review_block.findAll('img', class_='business-review-media__item-img')
                photos = [photo_block.get('src') for photo_block in photos_blocks]

                reviews.append({
                    'rating': stars,
                    'created_at': created_at_str,
                    'review_text': text,
                    'author_name': author,
                    'author_avatar_url': author_avatar,
                    'review_photos': photos,
                })

            return reviews

        return []
    except Exception:
        return []


def yandex_reviews_model():
    try:
        YandexReview.objects.all().delete()

        companies = YandexInformation.objects.all()

        for company in companies:
            organization_slug = company.organization_slug
            organization_id = company.organization_id

            result = get_yandex_reviews_data(organization_slug, organization_id)

            for res in result:
                review = YandexReview(
                    company=company.company,
                    rating=res.get('rating', ''),
                    created_at=res.get('created_at', ''),
                    review_text=res.get('review_text', ''),
                    author_name=res.get('author_name', ''),
                    author_avatar_url=res.get('author_avatar_url', ''),
                    review_photos=', '.join(res.get('review_photos', '')),
                )
                review.save()

    except Exception as e:
        print(e)


def yandex_company_model():
    try:
        YandexCompanyData.objects.all().delete()

        companies = YandexInformation.objects.all()

        for company in companies:
            organization_slug = company.organization_slug
            organization_id = company.organization_id

            result = get_yandex_company_data(organization_slug, organization_id)

            company_data = YandexCompanyData(
                company=company.company,
                average_rating=result.get('average_rating', ''),
                reviews_count=result.get('reviews_count', '')
            )
            company_data.save()

    except Exception as e:
        print(e)
