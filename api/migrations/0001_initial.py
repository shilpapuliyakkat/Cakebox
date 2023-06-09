# Generated by Django 4.1.6 on 2023-04-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cakebox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shape', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(default=True, upload_to='images')),
                ('weight', models.CharField(max_length=150)),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]
