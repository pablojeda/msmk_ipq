# Generated by Django 3.1.1 on 2021-01-15 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PistasPadel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('club', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('is_free', models.BooleanField(default=True)),
                ('pista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pistas.pistaspadel')),
            ],
        ),
    ]
