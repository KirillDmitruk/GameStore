from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='название продукта', unique=True, **NULLABLE)
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_of_product = models.IntegerField(verbose_name='цена за товар')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')
    owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца", **NULLABLE,
                              on_delete=models.SET_NULL)

    is_published = models.BooleanField(default=False, **NULLABLE, verbose_name='is_published')

    def __str__(self):
        return (f'{self.product_name} {self.photo}'
                f'{self.description} {self.price_of_product} Руб.'
                f'{self.created_at} {self.updated_at}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('can_edit_is_published', 'Can edit is published'),
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category')
        ]


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название статьи')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='URL')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='фото')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    sign_of_publication = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продукт')
    version = models.PositiveIntegerField(verbose_name='версия')
    title = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак активной версии')

    def __str__(self):
        return f'{self.product}.'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продуктов'
