from vl.utils.services import vl_reviews_model, vl_company_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка отзывов с Vl'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        vl_reviews_model()
        vl_company_model()
        print('Загрузка завершилась')