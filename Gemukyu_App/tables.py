import django_tables2 as tables
from .models import Games

class GamesTable(tables.Table):
    class Meta:
        model = Games
        template_name = "django_tables2/bootstrap.html" #there are multiple bootstrap types in django_tables2 - experiment with diff versions
        fields = ("small_pic", "title", "genre", "release_date", "price")