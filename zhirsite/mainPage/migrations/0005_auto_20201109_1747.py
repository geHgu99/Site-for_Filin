# Generated by Django 3.1.2 on 2020-11-09 14:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_auto_20201109_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurements',
            options={'ordering': ['data']},
        ),
        migrations.AlterModelManagers(
            name='measurements',
            managers=[
                ('measure', django.db.models.manager.Manager()),
            ],
        ),
    ]