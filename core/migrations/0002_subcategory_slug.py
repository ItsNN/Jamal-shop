# Generated by Django 5.0 on 2023-12-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='2', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
