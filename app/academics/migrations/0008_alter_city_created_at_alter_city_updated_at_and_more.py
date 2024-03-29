# Generated by Django 5.0.2 on 2024-03-22 22:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0007_student_delete_students_alter_city_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='identification_type',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='identification_type',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='person',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.user'),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 136990)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 121364)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 6, 26, 121364)),
        ),
    ]
