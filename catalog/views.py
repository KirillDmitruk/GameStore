from django.db.models import Prefetch
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import GameForm, VersionProductForm
from catalog.models import Product, Category, Blog, Version


class HomeListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # prefetch_related для оптимизации запросов к базе данных,
        # чтобы получить все связанные объекты VersionProduct для каждого Product
        # При помощи Prefetch (предварительная выборка):
        # versionproduct_set - формсет модели VersionProduct
        # queryset - набор запросов (в данном случае устанавливаем фильтр, чтобы получать
        # только активные версии)

        products_with_versions = Product.objects.prefetch_related(
            Prefetch(
                "versionproduct_set",
                queryset=Version.objects.filter(is_active=True),
            )
        ).all()

        # Добавляем эту отфильтрованную информацию в контекст
        context_data["products_with_versions"] = products_with_versions
        return context_data


class ContactDetailView(DetailView):
    model = Product


class GameDetailView(DetailView):
    model = Product


class GenresListView(ListView):
    model = Category


class GameCreateView(CreateView):
    model = Product
    form_class = GameForm
    success_url = reverse_lazy('catalog:games_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class GameUpdateView(UpdateView):
    model = Product
    form_class = GameForm
    success_url = reverse_lazy('catalog:games_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(
            Product, Version, form=VersionProductForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.product_name)
            new_blog.save()

        return super().form_valid(form)

    def form_valid_formset(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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
    slug_field = 'slug'
    fields = ['title', 'description', 'photo']

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
