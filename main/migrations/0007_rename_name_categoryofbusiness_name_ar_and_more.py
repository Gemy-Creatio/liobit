# Generated by Django 4.0.4 on 2022-05-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_projects_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryofbusiness',
            old_name='Name',
            new_name='Name_ar',
        ),
        migrations.RenameField(
            model_name='categoryofbusiness',
            old_name='description',
            new_name='description_ar',
        ),
        migrations.AddField(
            model_name='categoryofbusiness',
            name='Name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='categoryofbusiness',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]