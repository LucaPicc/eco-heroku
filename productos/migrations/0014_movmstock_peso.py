# Generated by Django 3.1.2 on 2020-10-13 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_movpstock_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='movmstock',
            name='peso',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
