# Generated by Django 4.0.5 on 2022-06-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoodapp', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborhoodapp.neighborhood'),
        ),
    ]