# Generated by Django 3.2.20 on 2023-08-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20230816_0937'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
