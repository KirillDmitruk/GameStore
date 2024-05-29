from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class GameForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'photo', 'category', 'price_of_product', 'slug', 'owner',)

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if product_name in FORBIDDEN_WORDS:
            raise ValidationError('Нельзя использовать запрещенные слова')
        return product_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description in FORBIDDEN_WORDS:
            raise ValidationError('Нельзя использовать запрещенные слова')
        return description


class VersionProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version', 'title', 'is_active',)
