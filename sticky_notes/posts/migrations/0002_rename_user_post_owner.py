# Generated by Django 5.0.6 on 2024-06-15 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="user",
            new_name="owner",
        ),
    ]
