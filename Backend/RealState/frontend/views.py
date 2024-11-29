from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from properties.models import Category, Property, PropertyImages



class Index(generic.ListView):
    model = Property
    queryset = Property.objects.all()
    template_name ='frontend/index.html'
    context_object_name ='properties'

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['available_properties'] = self.get_queryset()
        context['highlighted_properties'] = self.get_queryset().filter(is_highlight=True)
        return context


class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'frontend/property_detail.html'
    slug_field ='slug'
    context_object_name = 'property_detail'
