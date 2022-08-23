from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tz.tbc import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
