# Generated by Django 3.1.3 on 2021-01-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201206_2234'),
        ('store', '0017_auto_20210105_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('WRS', 'WORST'), ('BAD', 'BAD'), ('GOD', 'GOOD')], max_length=3)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.users')),
            ],
        ),
    ]
