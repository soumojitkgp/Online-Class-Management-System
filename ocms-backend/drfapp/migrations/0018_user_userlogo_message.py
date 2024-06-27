# Generated by Django 4.1.3 on 2023-03-30 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("drfapp", "0017_course_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="userlogo",
            field=models.CharField(default="", max_length=1),
        ),
        migrations.CreateModel(
            name="message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("msg", models.TextField()),
                ("senttime", models.DateTimeField()),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="drfapp.user",
                    ),
                ),
                (
                    "sendercourse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="drfapp.course",
                    ),
                ),
            ],
        ),
    ]