# Generated by Django 4.2.7 on 2024-09-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_item_category_item_label"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="slug",
            field=models.SlugField(default="test-product"),
            preserve_default=False,
        ),
    ]
