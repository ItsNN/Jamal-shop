# Generated by Django 5.0 on 2023-12-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_menuitem_available_menuitem_discounted_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(default='hot-coffee', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
