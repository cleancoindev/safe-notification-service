# Generated by Django 2.2 on 2019-04-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0006_auto_20190412_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='version_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]