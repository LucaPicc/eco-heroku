# Generated by Django 3.1 on 2020-09-02 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200901_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de producto')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción de producto')),
                ('material', models.CharField(max_length=50, verbose_name='Material por el cual es compuesto')),
                ('cantkg', models.DecimalField(decimal_places=3, max_digits=5)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.entity')),
            ],
        ),
    ]
