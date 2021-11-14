from django.urls import path

from .views import SalesListView


urlpatterns = [
    path('', SalesListView.as_view(), name='index'),
]
