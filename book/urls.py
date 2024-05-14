from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from book.api.v1.views import PersonModelViewSet


router = routers.DefaultRouter()
router.register('persons', PersonModelViewSet, basename='person')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
