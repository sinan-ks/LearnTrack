# Generated by Django 5.0.6 on 2024-06-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHub', '0002_student_email_student_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
