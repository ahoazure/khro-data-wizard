# Generated by Django 2.1.7 on 2019-03-05 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_wizard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='loader',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]