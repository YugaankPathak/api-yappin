# Generated by Django 5.1.1 on 2024-09-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_user_age_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='not specified', max_length=20, null=True),
        ),
    ]
