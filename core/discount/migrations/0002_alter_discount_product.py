# Generated by Django 5.0 on 2024-01-29 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
        ('shop', '0007_alter_rating_star_remove_rating_ip_rating_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='shop.product'),
        ),
    ]
