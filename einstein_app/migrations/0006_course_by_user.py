# Generated by Django 3.0.5 on 2020-07-02 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('einstein_app', '0005_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='by_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
