from django.contrib import admin
from twoGis.models import GisReview, GisInformation, GisCompanyData

admin.site.register(GisInformation)
admin.site.register(GisReview)
admin.site.register(GisCompanyData)
