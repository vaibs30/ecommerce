# Generated by Django 3.0.8 on 2020-07-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200706_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='list_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
