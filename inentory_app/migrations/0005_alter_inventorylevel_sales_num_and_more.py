# Generated by Django 5.1.2 on 2024-12-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inentory_app', '0004_inventorylevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylevel',
            name='sales_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventorylevel',
            name='stock_range',
            field=models.IntegerField(),
        ),
    ]
