# Generated by Django 5.1 on 2024-10-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_makanan', '0009_menuitem_image_url_menu'),
        ('manajemen_pesanan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='items',
            field=models.ManyToManyField(to='cards_makanan.menuitem'),
        ),
    ]
