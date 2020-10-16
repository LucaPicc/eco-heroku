# Generated by Django 3.1 on 2020-09-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20200918_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cant',
        ),
        migrations.AddField(
            model_name='materialstock',
            name='descripcion',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='descripcion',
            field=models.CharField(default='', max_length=250, null=True, verbose_name='Descripción de producto'),
        ),
    ]