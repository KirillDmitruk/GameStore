# Generated by Django 4.2.2 on 2024-06-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='менеджер'),
        ),
    ]
