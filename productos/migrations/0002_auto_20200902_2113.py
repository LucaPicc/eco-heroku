# Generated by Django 3.1 on 2020-09-03 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200901_1910'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cant',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cantkg',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
        migrations.CreateModel(
            name='Movimient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.entity')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='productos.product')),
            ],
        ),
    ]
