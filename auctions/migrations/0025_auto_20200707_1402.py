# Generated by Django 3.0.8 on 2020-07-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20200707_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Electronics', 'Electronics'), ('Kitchen', 'Kitchen'), ('Others', 'Others')], max_length=12),
        ),
    ]