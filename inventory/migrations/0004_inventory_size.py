# Generated by Django 4.2.7 on 2023-11-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_inventory_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="size",
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]