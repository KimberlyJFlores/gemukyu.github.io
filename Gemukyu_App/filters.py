import django_filters
from .models import Games

class GamesFilter(django_filters.FilterSet):
    class Meta:
        model = Games
        fields = {'title': ["exact", "contains"], 'description': ["contains"], 'genre': ["exact"], 
                  'release_date': ["contains"], 'price': ["exact", "contains"]}