# Generated by Django 3.2.9 on 2021-11-19 20:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
