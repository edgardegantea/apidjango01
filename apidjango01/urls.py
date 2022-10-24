from django.contrib import admin
from django.urls import path, include
from employee import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('employeedetails', views.Employee)

urlpatterns = [
    path('', include(router.urls)),
]
