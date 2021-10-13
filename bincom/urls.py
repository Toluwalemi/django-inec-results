from django.urls import path
from .views import HomePageView, polling_unit_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('polling-results/', polling_unit_view, name='polling-results')
]
