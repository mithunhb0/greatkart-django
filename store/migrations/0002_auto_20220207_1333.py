# Generated by Django 3.2 on 2022-02-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reviewrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductGallery',
        ),
        migrations.DeleteModel(
            name='ReviewRating',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]