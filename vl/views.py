from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from vl.models import VlInformation, VlReview, VlCompanyData


@require_GET
def vl_reviews_api(request):
    company = request.GET.get('company', '')
    cnt = int(request.GET.get('cnt', 10))
    min_rating = int(request.GET.get('min_rating', 4))

    reviews_list = []

    if company:
        reviews = VlReview.objects.filter(company=company, rating__gte=min_rating)

        for review in reviews:
            if review.review_photos:

                reviews_list.append({
                    'rating': review.rating,
                    'created_at': review.created_at,
                    'review_text': review.review_text,
                    'author_name': review.author_name,
                    'author_avatar_url': review.author_avatar_url,
                    'photos': review.review_photos.split(', '),
                })

        return JsonResponse({'reviews': reviews_list[:cnt]}, status=200)

    else:
        return JsonResponse({'reviews': []}, status=400)


@require_GET
def vl_company_api(request):
    company = request.GET.get('company', '')

    if company:
        company_data = VlCompanyData.objects.filter(company=company).first()

        if company_data:
            return JsonResponse({'average_rating': company_data.average_rating, 'reviews_count': company_data.reviews_count}, status=200)
        else:
            return JsonResponse({'average_rating': None, 'reviews_count': None}, status=400)

    else:
        return JsonResponse({'average_rating': None, 'reviews_count': None}, status=400)