# Generated by Django 5.1.3 on 2024-11-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('infotainment', 'Infotainment'), ('entertainment', 'Entertainment'), ('education', 'Education')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='uploads/audio/')),
                ('text_file', models.FileField(blank=True, null=True, upload_to='uploads/text/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='uploads/video/')),
            ],
        ),
    ]
