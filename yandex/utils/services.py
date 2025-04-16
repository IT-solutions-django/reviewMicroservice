import requests
from bs4 import BeautifulSoup
from yandex.utils.setting import SettingRequest
from django.http import JsonResponse
from django.views.decorators.http import require_GET


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
        reviews_limit: int,
        min_rating: int
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
                stars = len(review_block.find('div', class_='business-rating-badge-view__stars').findAll('span'))

                created_at_str = review_block.find('span', class_='business-review-view__date').find('span').text

                author_avatar = review_block.find('div', class_='user-icon-view__icon').get('style')
                if author_avatar:
                    author_avatar = author_avatar.split('url(')[1][:-1]

                photos_blocks = review_block.findAll('img', class_='business-review-media__item-img')
                photos = [photo_block.get('src') for photo_block in photos_blocks]

                if stars >= min_rating:
                    reviews.append({
                        'rating': stars,
                        'created_at': created_at_str,
                        'review_text': text,
                        'author_name': author,
                        'author_avatar_url': author_avatar,
                        'review_photos': photos,
                    })

            return reviews[:reviews_limit]

        return []
    except Exception:
        return []


@require_GET
def yandex_reviews_api(request):
    try:
        organization_slug = request.GET.get('organization_slug')
        organization_id = str(request.GET.get('organization_id'))
        reviews_limit = int(request.GET.get('limit', 10))
        min_rating = int(request.GET.get('min_rating', 4))

        if organization_slug and organization_id:
            result = get_yandex_reviews_data(organization_slug, organization_id, reviews_limit, min_rating)
            return JsonResponse({'reviews': result}, status=200)
        else:
            return JsonResponse({'reviews': []}, status=400)
    except Exception:
        return JsonResponse({'reviews': []}, status=400)


@require_GET
def yandex_company_api(request):
    try:
        organization_slug = request.GET.get('organization_slug')
        organization_id = str(request.GET.get('organization_id'))

        if organization_slug and organization_id:
            result = get_yandex_company_data(organization_slug, organization_id)
            return JsonResponse({'company_data': result}, status=200)
        else:
            return JsonResponse({'company_data': []}, status=400)
    except Exception:
        return JsonResponse({'company_data': []}, status=400)
