# Generated by Django 4.2 on 2023-04-22 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=250)),
                ('key_word1', models.CharField(blank=True, max_length=100, null=True)),
                ('key_word2', models.CharField(blank=True, max_length=100, null=True)),
                ('key_word3', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('body', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('is_pulished', models.BooleanField(default=True)),
                ('authar_name', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.categories')),
            ],
        ),
    ]
