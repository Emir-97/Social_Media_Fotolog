# Generated by Django 3.2.5 on 2021-08-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]