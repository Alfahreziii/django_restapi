# Generated by Django 5.1 on 2024-10-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_makanan', '0005_makanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
