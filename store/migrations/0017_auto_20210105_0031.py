# Generated by Django 3.1.2 on 2021-01-05 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201206_2234'),
        ('store', '0016_remove_orderitem_customerinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='users.users'),
        ),
    ]
