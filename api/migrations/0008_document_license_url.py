# Generated by Django 2.1 on 2019-09-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190903_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='license_url',
            field=models.TextField(default='http://open5e.com/legal'),
        ),
    ]
