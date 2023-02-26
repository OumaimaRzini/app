# Generated by Django 4.1.5 on 2023-02-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('telephone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]