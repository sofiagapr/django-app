# Generated by Django 5.0.2 on 2024-03-15 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_remove_user_age_remove_user_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 39, 21, 160507)),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 39, 21, 160507)),
        ),
    ]