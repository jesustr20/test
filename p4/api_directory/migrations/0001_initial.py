# Generated by Django 3.1.2 on 2020-10-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('archivo', models.FileField(upload_to='media')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
