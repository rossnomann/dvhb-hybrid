# Generated by Django 3.2 on 2021-04-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20210330_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='oauth_info',
            field=models.JSONField(default=dict, null=True, verbose_name='OAuth information'),
        ),
    ]