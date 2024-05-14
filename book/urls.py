from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from book.api.v1.views import PersonModelViewSet, PhoneModelViewSet


router = routers.DefaultRouter()
router.register('persons', PersonModelViewSet, basename='person')
router.register('phones', PhoneModelViewSet, basename='phone')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
