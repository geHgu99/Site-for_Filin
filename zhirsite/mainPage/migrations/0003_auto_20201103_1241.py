# Generated by Django 3.1.2 on 2020-11-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20201103_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='measurements_data',
            field=models.DateField(),
        ),
    ]