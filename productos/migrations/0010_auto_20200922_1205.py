# Generated by Django 3.1 on 2020-09-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20200922_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.product'),
        ),
    ]
