from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Category, Blog


class HomeListView(ListView):
    model = Product


# def home(request):
#     game_list = Product.objects.all()
#     context = {
#         'object_list': game_list,
#         'title': 'CityGames'
#     }
#     return render(request, 'catalog/product_list.html', context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name} ({phone}): {message}')
#
#     return render(request, 'catalog/contact_detail.html')


class ContactDetailView(DetailView):
    model = Product


class GameDetailView(DetailView):
    model = Product


# def game_detail(request, pk):
#     context = {
#         'object': Product.objects.get(id=pk)
#     }
#     return render(request, 'catalog/product_detail.html', context)


class GenresListView(ListView):
    model = Category


# def genres(request):
#     genres_list = Category.objects.all()
#     context = {
#         'object_list': genres_list
#     }
#     return render(request, 'catalog/category_list.html', context)


class GameCreateView(CreateView):
    model = Product
    fields = ['product_name', 'description', 'photo', 'category', 'price_of_product']
    success_url = reverse_lazy('catalog:games_list')


class GameUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'description', 'photo', 'category', 'price_of_product']
    success_url = reverse_lazy('catalog:games_list')


class GameDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:games_list')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'description', 'photo']
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'description', 'photo']

    # success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
