# Generated by Django 3.1.3 on 2021-01-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20210127_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_recommendations',
            field=models.IntegerField(default='0'),
        ),
    ]
