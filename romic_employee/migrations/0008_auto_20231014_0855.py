# Generated by Django 3.2.12 on 2023-10-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romic_employee', '0007_delete_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Amount6',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='status6',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]