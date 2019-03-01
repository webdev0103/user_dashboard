# Generated by Django 2.1 on 2018-08-16 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haikuapp', '0014_delete_img_ulr_from_card_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='file_from_server',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='template',
            name='server_image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='useractivate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to=settings.AUTH_USER_MODEL),
        ),
    ]
