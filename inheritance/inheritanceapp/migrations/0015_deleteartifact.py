# Generated by Django 4.0 on 2022-01-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritanceapp', '0014_alter_artifact_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteArtifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
