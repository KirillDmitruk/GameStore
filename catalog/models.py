from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_of_product = models.IntegerField(verbose_name='цена за товар')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return (f'{self.product_name} {self.photo}'
                f'{self.description} {self.price_of_product} Руб.'
                f'{self.created_at} {self.updated_at}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название статьи')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='ссылка')
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
