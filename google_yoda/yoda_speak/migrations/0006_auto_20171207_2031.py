# Generated by Django 2.0 on 2017-12-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoda_speak', '0005_yodaphrase_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yodaphrase',
            name='url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
