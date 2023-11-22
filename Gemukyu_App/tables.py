import django_tables2 as tables
from django.utils.html import format_html
from .models import Games

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html(
            '<img src="/static/images/{url}" height="50px", width="50px">',
            url=value
        )

class GamesTable(tables.Table):
    small_pic = ImageColumn()

    class Meta:
        model = Games
        row_attrs = {
            "onClick": lambda record: "document.location.href='/game_page/{0}';".format(record.game_id)
        }
        template_name = "django_tables2/bootstrap.html" #there are multiple bootstrap types in django_tables2 - experiment with diff versions
        fields = ("small_pic", "title", "genre", "release_date", "price")
