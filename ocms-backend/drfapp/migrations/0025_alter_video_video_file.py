# Generated by Django 4.1.3 on 2023-04-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0024_rename_video_video_video_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_file",
            field=models.FileField(upload_to=""),
        ),
    ]
