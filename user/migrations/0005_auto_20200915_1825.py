# Generated by Django 3.1 on 2020-09-15 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200904_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='loc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Localidad'),
        ),
        migrations.AddField(
            model_name='entity',
            name='prov',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='tipo',
            field=models.CharField(choices=[('EM', 'Empresa'), ('MU', 'Municipio'), ('RE', 'Recicladora'), ('CO', 'Cooperativa'), ('PU', 'Punto Limpio')], default='', max_length=2),
        ),
        migrations.CreateModel(
            name='ProfilePunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propiedad', models.CharField(choices=[('ES', 'Estado'), ('PR', 'Privada')], max_length=50, verbose_name='Propiedad del estado o privado')),
                ('operacion', models.CharField(choices=[('MU', 'Municipal'), ('PR', 'Privada')], max_length=50, verbose_name='Operación municipal o privada')),
                ('ton_recup', models.DecimalField(decimal_places=2, max_digits=10)),
                ('visitas', models.IntegerField(verbose_name='Cantidad de visitas por año')),
                ('gast_op', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cant_personas', models.IntegerField()),
                ('punt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.entity')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileMun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hab', models.IntegerField()),
                ('dispo_final', models.CharField(choices=[('VE', 'Vertedero'), ('VC', 'Vertedero Controlado'), ('RS', 'Relleno Sanitario')], max_length=2)),
                ('difreco', models.BooleanField(default=False)),
                ('complejo_tratamiento', models.BooleanField(default=False)),
                ('compostaje_biodigestion', models.BooleanField(default=False)),
                ('planta_clasif', models.BooleanField(default=False)),
                ('otros', models.BooleanField(default=False)),
                ('ton_recup', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pers_recol', models.IntegerField()),
                ('pers_comp_am', models.IntegerField()),
                ('ton_proces', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cost_recol', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cost_comp_am', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ing_venta', models.DecimalField(decimal_places=2, max_digits=20)),
                ('mun', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.entity')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_socio', models.IntegerField()),
                ('fuent_rec', models.CharField(choices=[('IN', 'Industria/Privado'), ('DO', 'Domiciliario'), ('MI', 'Mix')], max_length=2)),
                ('recol', models.BooleanField(default=False)),
                ('empl', models.IntegerField()),
                ('ton_rec', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ton_a_rechazo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gast_totales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.entity')),
            ],
        ),
    ]
