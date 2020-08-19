# Generated by Django 3.0.8 on 2020-07-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200706_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='cprice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='description',
            field=models.CharField(default='desc', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='imageURL',
            field=models.URLField(default='no'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='title',
            field=models.CharField(default='vaibav', max_length=20),
            preserve_default=False,
        ),
    ]