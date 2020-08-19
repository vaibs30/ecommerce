# Generated by Django 3.0.8 on 2020-07-06 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200706_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]