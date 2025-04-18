from django.contrib import admin
from yandex.models import YandexReview, YandexInformation, YandexCompanyData

admin.site.register(YandexInformation)
admin.site.register(YandexReview)
admin.site.register(YandexCompanyData)
