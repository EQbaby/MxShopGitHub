# Generated by Django 2.0.6 on 2018-10-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20181008_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_font_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
    ]
