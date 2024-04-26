# Generated by Django 5.0.2 on 2024-03-17 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0010_students_alter_person_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='identification_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 407124))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 407124))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 404660)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 407124)),
        ),
        migrations.AlterField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 407124)),
        ),
        migrations.AlterField(
            model_name='students',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 407124)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 402103)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 22, 54, 13, 402103)),
        ),
    ]
