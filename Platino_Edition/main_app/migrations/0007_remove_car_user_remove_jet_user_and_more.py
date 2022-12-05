# Generated by Django 4.1.3 on 2022-12-04 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_car_user_jet_user_realestate_user_yacht_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.RemoveField(
            model_name='jet',
            name='user',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='yacht',
            name='user',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
                ('jets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jet')),
                ('realestates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.realestate')),
                ('yachts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.yacht')),
            ],
        ),
    ]