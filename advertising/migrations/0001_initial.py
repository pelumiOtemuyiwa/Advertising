# Generated by Django 4.0.6 on 2023-02-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisingcampaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('createdate', models.CharField(max_length=225)),
                ('totalbudget', models.CharField(max_length=225)),
                ('dailybudget', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
