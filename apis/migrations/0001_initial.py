# Generated by Django 3.2.12 on 2024-02-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]