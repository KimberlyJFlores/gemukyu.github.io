import django_filters
from django_filters import DateFilter, CharFilter

from .models import Games

class GamesFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    #start_date = DateFilter(field_name="release_date", lookup_expr='gte')
    #end_date = DateFilter(field_name="release_date", lookup_expr='lte')
    
    class Meta:
        model = Games
        fields = ['genre', 'price']