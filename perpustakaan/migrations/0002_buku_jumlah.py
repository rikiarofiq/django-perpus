# Generated by Django 3.2.7 on 2021-10-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jumlah',
            field=models.IntegerField(null=True),
        ),
    ]
