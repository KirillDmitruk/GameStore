from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactDetailView, HomeListView, GenresListView, GameDetailView, GameCreateView, \
    GameUpdateView, GameDeleteView, BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', HomeListView.as_view(), name='games_list'),
                  path('contacts/', ContactDetailView.as_view(), name='contacts'),
                  path('genres_list/', GenresListView.as_view(), name='genres'),
                  path('<int:pk>/game_detail/', GameDetailView.as_view(), name='game_detail'),
                  path('create/', GameCreateView.as_view(), name='game_create'),
                  path('<int:pk>/update', GameUpdateView.as_view(), name='game_update'),
                  path('<int:pk>/delete', GameDeleteView.as_view(), name='game_delete'),

                  path('blog/', BlogListView.as_view(), name='blog_list'),
                  path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
                  path('blog/<slug:slug>/detail', BlogDetailView.as_view(), name='blog_detail'),
                  path('blog/<slug:slug>/update', BlogUpdateView.as_view(), name='blog_update'),
                  path('blog/<slug:slug>/delete', BlogDeleteView.as_view(), name='blog_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
