# Generated by Django 3.2.12 on 2023-10-14 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('romic_employee', '0008_auto_20231014_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='servicetitle2',
            new_name='servicecategory',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='servicedescription',
            new_name='servicedescription1',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_main_img2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_main_img3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='servicetitle3',
        ),
    ]
