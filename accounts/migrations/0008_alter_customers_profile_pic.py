# Generated by Django 4.1.2 on 2022-11-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customers_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profileicon.jpg', null=True, upload_to=''),
        ),
    ]
