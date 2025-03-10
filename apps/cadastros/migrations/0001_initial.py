# Generated by Django 4.2.2 on 2023-06-19 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CamposModel",
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
                ("nome", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, editable=False, unique=True)),
                (
                    "texto_ajuda",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "unico",
                    models.BooleanField(default=False, verbose_name="Campo único"),
                ),
                (
                    "obrigatorio",
                    models.BooleanField(
                        default=False, verbose_name="Campo obrigatório"
                    ),
                ),
                ("ativo", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Campo",
                "verbose_name_plural": "Campos",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="PropostasModel",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Aguardando análise", "Aguardando análise"),
                            ("Aprovada", "Aprovada"),
                            ("Reprovada", "Reprovada"),
                        ],
                        default="Aguardando análise",
                        max_length=20,
                    ),
                ),
                ("avaliada", models.BooleanField(default=False)),
                (
                    "data_registro",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de registro"
                    ),
                ),
                (
                    "data_avaliacao",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Data de avaliação"
                    ),
                ),
            ],
            options={
                "verbose_name": "Proposta",
                "verbose_name_plural": "Propostas",
                "ordering": ["data_registro"],
            },
        ),
        migrations.CreateModel(
            name="RespostasCamposModels",
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
                (
                    "resposta",
                    models.CharField(max_length=250, verbose_name="Resposta do campo"),
                ),
                (
                    "campo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respostas_campo",
                        to="cadastros.camposmodel",
                        verbose_name="Campo",
                    ),
                ),
                (
                    "proposta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respostas_proposta",
                        to="cadastros.propostasmodel",
                        verbose_name="Proposta",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resposta do campo",
                "verbose_name_plural": "Respostas dos campos",
                "ordering": ["campo"],
            },
        ),
    ]
