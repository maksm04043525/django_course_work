# Generated by Django 5.1.3 on 2024-11-20 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
