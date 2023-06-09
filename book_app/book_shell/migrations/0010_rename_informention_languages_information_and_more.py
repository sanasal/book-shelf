# Generated by Django 4.0.10 on 2023-05-17 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_shell', '0009_languages_informention_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languages',
            old_name='informention',
            new_name='information',
        ),
        migrations.RenameField(
            model_name='mystry_and_police',
            old_name='informention',
            new_name='information',
        ),
        migrations.RenameField(
            model_name='programming',
            old_name='informention',
            new_name='information',
        ),
        migrations.RenameField(
            model_name='psychology',
            old_name='informention',
            new_name='information',
        ),
        migrations.RenameField(
            model_name='sciences',
            old_name='informention',
            new_name='information',
        ),
        migrations.AddField(
            model_name='islam',
            name='information',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='add_comment',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report_issue',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
