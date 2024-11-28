from django.urls import path
from . import views
from .views import Index,PropertyDetail
app_name ='frontend'

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('property/detail/<slug:slug>', PropertyDetail.as_view(), name='property_detail'),
]