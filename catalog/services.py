from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_genres_from_cache():
    """Получает данные по категориям из кэша, если кэш пуст, получает данные из бд."""
    if not CACHE_ENABLED:  # если кэш не включен в проект
        return Category.objects.all()  # возвращаем все категории

    key = 'genres_list'
    cache_genres = cache.get(key)  # получаем кэш по ключу
    if cache_genres is not None:  # если кэш не пустой
        return cache_genres  # возвращаем кэш
    else:
        genres = Category.objects.all()  # получаем все категории
        cache.set(key, genres)  # сохраняем кэш
        return genres  # возвращаем кэш категории
