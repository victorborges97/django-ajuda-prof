# Generated by Django 3.2.9 on 2021-11-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.author'),
        ),
    ]
