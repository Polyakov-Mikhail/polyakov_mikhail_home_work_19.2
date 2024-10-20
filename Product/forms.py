from django import forms
from django.forms import BooleanField

from Product.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'is_published')

    def clean_name(self):

        cleaned_data = self.cleaned_data['name']
        cleaned_data_lower = cleaned_data.lower()

        forbidden_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                                'радар']

        for word in forbidden_words_list:
            if word in cleaned_data_lower:
                raise forms.ValidationError('Торвар с таким названием запрещен к продадаже на этой площадке')

        return cleaned_data

    def clean_description(self):

        cleaned_data = self.cleaned_data['description']
        cleaned_data_lower = cleaned_data.lower()

        bad_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар']
        for word in bad_words_list:
            if word in cleaned_data_lower:
                raise forms.ValidationError('Торвар с таким описанием запрещен к продадаже на этой площадке')

        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
