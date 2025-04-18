from django.db import models


class VlInformation(models.Model):
    company = models.TextField(verbose_name='Компания')
    organization_slug = models.TextField(verbose_name='slug организации')
    organization_id = models.TextField(verbose_name='id организации')

    def __str__(self):
        return self.company


class VlReview(models.Model):
    company = models.TextField(verbose_name='Компания', null=True, blank=True)
    rating = models.TextField(verbose_name='Рейтинг', null=True, blank=True)
    created_at = models.TextField(verbose_name='Дата', null=True, blank=True)
    review_text = models.TextField(verbose_name='Отзыв', null=True, blank=True)
    author_name = models.TextField(verbose_name='Автор', null=True, blank=True)
    author_avatar_url = models.TextField(verbose_name='Аватарка автора', null=True, blank=True)
    review_photos = models.TextField(verbose_name='Фотографии', null=True, blank=True)

    def __str__(self):
        return f'{self.company} | {self.review_text}'


class VlCompanyData(models.Model):
    company = models.TextField(verbose_name='Компания', null=True, blank=True)
    average_rating = models.TextField(verbose_name='Средний рейтинг', null=True, blank=True)
    reviews_count = models.TextField(verbose_name='Кол-во отзывов', null=True, blank=True)

    def __str__(self):
        return f'{self.company} | {self.average_rating} | {self.reviews_count}'




