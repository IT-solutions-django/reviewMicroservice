from twoGis.utils.services import two_gis_reviews_model, two_gis_company_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка отзывов с 2GIS'

    def handle(self, *args, **kwargs):
        print('Загрузка началась')
        two_gis_reviews_model()
        two_gis_company_model()
        print('Загрузка завершилась')