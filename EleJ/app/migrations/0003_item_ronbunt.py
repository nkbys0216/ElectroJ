# Generated by Django 2.1.1 on 2019-04-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_ronbun'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ronbunt',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='論文タイトル'),
        ),
    ]