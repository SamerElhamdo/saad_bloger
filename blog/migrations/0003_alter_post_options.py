# Generated by Django 3.2.5 on 2021-07-15 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210714_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'verbose_name': 'Post', 'verbose_name_plural': 'posts'},
        ),
    ]
