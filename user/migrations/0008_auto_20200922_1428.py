# Generated by Django 3.1 on 2020-09-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200918_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemun',
            name='pers_clas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemun',
            name='pers_recol',
            field=models.IntegerField(default=0, null=True),
        ),
    ]