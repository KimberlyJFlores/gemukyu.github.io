# Generated by Django 4.2.5 on 2023-11-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gemukyu_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='discount',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
    ]