# Generated by Django 2.0.4 on 2018-05-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cet46', '0004_img_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]