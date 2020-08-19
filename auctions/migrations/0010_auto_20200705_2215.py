# Generated by Django 3.0.8 on 2020-07-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200705_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='item_watchlist', to='auctions.listing'),
        ),
    ]