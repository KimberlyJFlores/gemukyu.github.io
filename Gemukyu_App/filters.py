import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import Games

class GamesFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    price_gte = NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = NumberFilter(field_name='price', lookup_expr='lte')
    #start_date = DateFilter(field_name="release_date", lookup_expr='gte')
    #end_date = DateFilter(field_name="release_date", lookup_expr='lte')
    
    class Meta:
        model = Games
        fields = []