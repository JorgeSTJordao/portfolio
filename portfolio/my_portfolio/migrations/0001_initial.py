# Generated by Django 5.2 on 2025-04-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evento",
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
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
                ("data_inicio", models.DateField()),
                ("concluido", models.BooleanField(default=False)),
                ("ano", models.IntegerField()),
                ("ordem", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ["ano", "ordem"],
            },
        ),
    ]
