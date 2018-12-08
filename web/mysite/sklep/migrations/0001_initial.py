# Generated by Django 2.1.4 on 2018-12-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=18)),
                ('opis', models.TextField()),
                ('dostepnosc', models.BooleanField()),
            ],
        ),
    ]
