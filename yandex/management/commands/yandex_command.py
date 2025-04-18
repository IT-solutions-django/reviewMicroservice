from yandex.utils.services import yandex_reviews_model, yandex_company_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка отзывов с Яндекс'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        yandex_reviews_model()
        yandex_company_model()
        print('Загрузка завершилась')