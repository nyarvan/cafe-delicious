from django import forms
from base_app.models import Dish, CategoryDish, Reviews

class FormCategoryDishs(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Name of category", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))

    position = forms.DecimalField(widget=forms.TextInput(attrs={
                                    'type': "number", 'name': 'position', "id": "position", 'class': 'form-control'
    }))

    class Meta:
        model = CategoryDish
        fields = ("name", 'is_visibility', 'position')

class FormDishs(forms.ModelForm):


    title = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "title", 'class': "form-control", 'id': "title",
                               'placeholder': "Title", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))
    ingredients = forms.CharField(widget=forms.TextInput(attrs={
                                'type': "text", 'name': "ingredients", 'class': "form-control", 'id': "ingredients",
                               'placeholder': "Ingredients", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
    }))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'type': "number",
                                                                    'name': "price", 'id': "price",
                                                                    'placeholder': "Price", 'step': "0.01"}))

    image = forms.FileField()

    description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",
                                                           'name': "description", 'rows': "5",
                                                           'placeholder': "Description"}))

    dish_order = forms.DecimalField(widget=forms.TextInput(attrs={'type': "number", 'class': "form-control",
                                                                    'name': "dish_order", 'id': "dish_order",
                                                                    'placeholder': "Dish order",
                                                                    'data-rule': "minlen:1",
                                                                    'data-msg': "Please enter at least 1 chars"}))

    class Meta:
        model = Dish
        fields = ('category', 'title', 'ingredients', 'price', 'image', 'description',
                  'dish_order', 'is_visibility', 'is_special',)