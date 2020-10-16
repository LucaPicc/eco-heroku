# Generated by Django 3.1 on 2020-09-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200915_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='tipo',
            field=models.CharField(choices=[('EM', 'Empresa'), ('MU', 'Municipio'), ('RE', 'Recicladora'), ('CO', 'Cooperativa'), ('PL', 'Punto Limpio')], default='', max_length=2),
        ),
    ]