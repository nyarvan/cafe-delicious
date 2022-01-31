from django.urls import path
from .views import base_app_view, add_review

app_name = 'base_app'

urlpatterns = [
    path('', base_app_view, name='base_app_view'),
    path('review/', add_review, name='add_review')
]

