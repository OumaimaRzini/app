# Generated by Django 4.1.5 on 2023-02-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chiffre_Affaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.DecimalField(decimal_places=4, max_digits=12)),
                ('periode', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fournisseur', models.CharField(max_length=50)),
                ('date_De_Emprunt', models.DateTimeField(auto_now_add=True)),
                ('Valeur_Dette', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_De_remboursement', models.DateTimeField()),
            ],
        ),
    ]
