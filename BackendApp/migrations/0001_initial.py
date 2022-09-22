# Generated by Django 4.1.1 on 2022-09-22 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "specialty",
                    models.CharField(max_length=50, verbose_name="Specialty"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("rol", models.CharField(max_length=50, verbose_name="Rol")),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("lastName", models.CharField(max_length=50, verbose_name="LastName")),
                ("cellPhone", models.CharField(max_length=50, verbose_name="Celular")),
                ("e_mail", models.EmailField(max_length=50, verbose_name="@mail")),
                ("address", models.CharField(max_length=50, verbose_name="Address")),
                (
                    "username",
                    models.CharField(
                        max_length=15, unique=True, verbose_name="Username"
                    ),
                ),
                ("password", models.CharField(max_length=256, verbose_name="Password")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="BackendApp.doctor",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
