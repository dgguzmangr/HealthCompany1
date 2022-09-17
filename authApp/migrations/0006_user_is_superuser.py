# Generated by Django 4.1.1 on 2022-09-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authApp", "0005_remove_user_is_superuser_alter_diagnostic_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
    ]
