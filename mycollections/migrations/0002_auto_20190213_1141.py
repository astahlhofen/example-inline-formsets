# Generated by Django 2.1.7 on 2019-02-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycollections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
