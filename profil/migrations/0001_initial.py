# Generated by Django 5.0 on 2023-12-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='img/')),
                ('t_yil', models.DateField()),
            ],
        ),
    ]
