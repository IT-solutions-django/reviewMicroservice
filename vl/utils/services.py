import requests
from bs4 import BeautifulSoup
from vl.utils.setting import SettingRequest
from django.http import JsonResponse
from django.views.decorators.http import require_GET


def get_vl_company_data(organization_slug, organization_id):
    try:
        headers = SettingRequest.headers.value

        api_review_avg = f'https://www.vl.ru/ajax/company-history-votes?companyId={organization_id}'
        response = requests.get(api_review_avg, headers=headers)
        if response.status_code == 200:
            data = response.json()
            average_rating_history: dict = data["history"]
            average_rating = list(average_rating_history.values())[0]
        else:
            average_rating = None

        url = f"https://www.vl.ru/commentsgate/ajax/thread/company/{organization_slug}/embedded"

        params = {
            "theme": "company",
            "appVersion": "2024101514104",
            "_dc": "0.32945840348689304",
            "pastafarian": "0fb682602c07c4ae9bdb8969e7c43add3b898f4e7b14548c8c2287a29032d6b1",
            "location": f"https://www.vl.ru/{organization_slug}#comments",
            "moderatorMode": "1"
        }

        cookies = SettingRequest.cookies.value

        response = requests.get(url, headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
            res = response.json()['data']['content']
            soup = BeautifulSoup(res, 'html.parser')
            reviews_count_block = soup.find('div', class_='cmt-thread-subscription')
            reviews_count = reviews_count_block.find('span', class_='count').text
        else:
            reviews_count = None

        return {'average_rating': average_rating, 'reviews_count': reviews_count}
    except Exception:
        return {'average_rating': None, 'reviews_count': None}


def get_vl_reviews_data(
        organization_slug: str,
        limit: int,
        min_rating: int
):
    """
    Параметры:
    organization_slug (str): Слаг компании на vl.ru. Пример: "naparili-dv"
    organization_id (int): ID компании на vl.ru. Пример: 444287
    limit (int): Максимальное количество отзывов
    min_rating (int): Минимальная оценка отзыва

    Возвращает:
    list[dict], float, int: Возвращает список отзывов, средний рейтинг компании и общее количество отзывов

    """
    try:
        url = f"https://www.vl.ru/commentsgate/ajax/thread/company/{organization_slug}/embedded"

        params = {
            "theme": "company",
            "appVersion": "2024101514104",
            "_dc": "0.32945840348689304",
            "pastafarian": "0fb682602c07c4ae9bdb8969e7c43add3b898f4e7b14548c8c2287a29032d6b1",
            "location": f"https://www.vl.ru/{organization_slug}#comments",
            "moderatorMode": "1"
        }

        headers = SettingRequest.headers.value

        cookies = SettingRequest.cookies.value

        response = requests.get(url, headers=headers, params=params, cookies=cookies)

        if response.status_code == 200:
            res = response.json()['data']['content']
            soup = BeautifulSoup(res, 'html.parser')

            best_comments_block = soup.find('div', class_='best-comments')

            review_elements = soup.find_all('li', {'data-type': 'review'})

            if best_comments_block:
                review_elements += best_comments_block.find_all('li')

            reviews = []

            for review in review_elements:
                star_rating = review.find('div', class_='star-rating')
                if star_rating:
                    star_rating = int(float(star_rating.find('div', class_='active')['data-value']) * 5)
                else:
                    continue

                user_avatar = review.find('div', class_='user-avatar').find('img')
                if user_avatar:
                    user_avatar = user_avatar['src']

                user_name_tag = review.find('span', class_='user-name')
                user_name = user_name_tag.text.strip() if user_name_tag else 'N/A'

                review_text_tag = review.find('div', class_='cmt-content').find('p', class_='comment-text')
                if review_text_tag and "Комментарий:" in review_text_tag.text:
                    review_text = review_text_tag.text.strip().split("Комментарий:", 1)[1].strip()
                else:
                    continue

                time_tag = review.find('span', class_='time')
                time_text = time_tag.text

                photos = []
                photos_block = review.find('div', class_='comment-images')
                if photos_block:
                    photos_elements = photos_block.find_all('a')
                    for photo_element in photos_elements:
                        photos.append(photo_element.get('href'))

                if star_rating >= min_rating:
                    reviews.append({
                        'rating': star_rating,
                        'created_at': time_text,
                        'review_text': review_text,
                        'author_name': user_name,
                        'author_avatar_url': user_avatar,
                        'photos': photos,
                    })

            return reviews[:limit]
        else:
            return []
    except Exception:
        return []


@require_GET
def vl_reviews_api(request):
    try:
        organization_slug = request.GET.get('organization_slug')
        reviews_limit = int(request.GET.get('limit', 10))
        min_rating = int(request.GET.get('min_rating', 4))

        if organization_slug:
            result = get_vl_reviews_data(organization_slug, reviews_limit, min_rating)
            return JsonResponse({'reviews': result}, status=200)
        else:
            return JsonResponse({'reviews': []}, status=400)
    except Exception:
        return JsonResponse({'reviews': []}, status=400)


@require_GET
def vl_company_api(request):
    try:
        organization_slug = request.GET.get('organization_slug')
        organization_id = str(request.GET.get('organization_id'))

        if organization_slug and organization_id:
            result = get_vl_company_data(organization_slug, organization_id)
            return JsonResponse({'company_data': result}, status=200)
        else:
            return JsonResponse({'company_data': []}, status=400)
    except Exception:
        return JsonResponse({'company_data': []}, status=400)