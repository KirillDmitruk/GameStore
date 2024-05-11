# Generated by Django 5.0.4 on 2024-05-10 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(verbose_name='версия')),
                ('title', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак активной версии')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия продукта',
                'verbose_name_plural': 'версии продуктов',
            },
        ),
    ]
