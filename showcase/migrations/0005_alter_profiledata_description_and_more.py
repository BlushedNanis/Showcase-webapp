# Generated by Django 4.0.6 on 2024-05-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0004_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='extra1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='extra2',
            field=models.TextField(),
        ),
    ]
