# Generated by Django 5.1.1 on 2024-11-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0035_project_ref_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="riskassessment",
            name="ref_id",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="reference id"
            ),
        ),
    ]
