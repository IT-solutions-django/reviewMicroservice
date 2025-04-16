"""
URL configuration for review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yandex.utils.services import yandex_reviews_api, yandex_company_api
from vl.utils.services import vl_reviews_api, vl_company_api
from twoGis.utils.services import two_gis_reviews_api, two_gis_company_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/yandex-reviews/', yandex_reviews_api, name='yandex-reviews'),
    path('api/yandex-company/', yandex_company_api, name='yandex-company'),

    path('api/vl-reviews/', vl_reviews_api, name='vl-reviews'),
    path('api/vl-company/', vl_company_api, name='vl-company'),

    path('api/twoGis-reviews/', two_gis_reviews_api, name='twoGis-reviews'),
    path('api/twoGis-company/', two_gis_company_api, name='twoGis-company')
]
