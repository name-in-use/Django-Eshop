# Generated by Django 3.1.3 on 2021-01-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_product_total_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_recommendations',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
