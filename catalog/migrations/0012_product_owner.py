# Generated by Django 4.2.2 on 2024-05-28 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0011_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите владельца', null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL,
                                    verbose_name='Владелец'),
        ),
    ]
