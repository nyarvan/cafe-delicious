import datetime

from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator

class CategoryDish(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    is_visibility = models.BooleanField(default=True)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ("position", )

    def __str__(self):
        return f"{self.name}: {self.position}"


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/dishes", filename)

    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    ingredients = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=get_file_name, default='images/dishes/d3422c5a-633f-4c20-9873-fb9f5e774dde.png')
    description = models.TextField(blank=True)
    dish_order = models.PositiveIntegerField()
    is_visibility = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)

    class Meta:
        ordering = ("dish_order",)

    def __str__(self):
        return f"{self.title}: {self.price}"

class Reservation(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')

    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    date = models.DateField()
    time = models.TimeField()
    count_people = models.PositiveIntegerField()
    message = models.TextField(max_length=500, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time',)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'

class Contact(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    upload = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-upload', )

    def __str__(self):
        return f'{self.subject} ({self.name}, {self.email})'

class Event(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/dishes", filename)

    title = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=get_file_name)
    description = models.TextField(max_length=500)
    list1 = models.CharField(max_length=200)
    list2 = models.CharField(max_length=200)
    list3 = models.CharField(max_length=200)
    description2 = models.TextField(max_length=500)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.title}'

class Gallery(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/gallery", filename)

    num = models.PositiveIntegerField(unique=True)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.num}'

class Chief(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/chief", filename)

    surname = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_file_name)
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()

    class Meta:
        ordering = ('post', )

    def __str__(self):
        return f'{self.surname} {self.name} - {self.post}'

class Reviews(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join("images/reviews", filename)

    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_file_name, default='images/dishes/d3422c5a-633f-4c20-9873-fb9f5e774dde.png')
    rating = models.PositiveIntegerField()
    review = models.TextField(max_length=300)
    upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-upload',)

    def __str__(self):
        return f'{self.name}, rating - {self.rating}'




