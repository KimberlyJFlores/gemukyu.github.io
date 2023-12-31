# Generated by Django 4.2.6 on 2023-11-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gemukyu_App', '0002_games_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='developer_id',
        ),
        migrations.RemoveField(
            model_name='games',
            name='publisher_id',
        ),
        migrations.AddField(
            model_name='games',
            name='dev_website',
            field=models.CharField(default='placeholder', max_length=500),
        ),
        migrations.AddField(
            model_name='games',
            name='developer',
            field=models.CharField(default='placeholder', max_length=255),
        ),
        migrations.AddField(
            model_name='games',
            name='pub_website',
            field=models.CharField(default='placeholder', max_length=500),
        ),
        migrations.AddField(
            model_name='games',
            name='publisher',
            field=models.CharField(default='placeholder', max_length=255),
        ),
    ]
