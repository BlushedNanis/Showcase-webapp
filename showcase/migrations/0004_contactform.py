# Generated by Django 4.0.6 on 2024-05-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_profiledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('career_opportunity', 'Career Opportunity'), ('collaboration_interest', 'Collaboration Interest'), ('technical_inquiry', 'Technical Inquiry'), ('general_comment', 'General Comment'), ('feedback', 'Feedback'), ('suggestions', 'Suggestions'), ('other', 'Other')], max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email_sent', models.BooleanField(default=False)),
                ('email_received', models.BooleanField(default=False)),
            ],
        ),
    ]
