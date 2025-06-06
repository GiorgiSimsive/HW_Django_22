from django.core.exceptions import ValidationError
from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Наименование товара'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Опешите товар'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        description = cleaned_data.get("description", "")
        combined_text = f"{name} {description}".lower()

        for word in FORBIDDEN_WORDS:
            if word in combined_text:
                raise forms.ValidationError(f"Запрещено использовать слово: '{word}'")

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название продукта содержит запрещённое слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание продукта содержит запрещённое слово: {word}")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price
