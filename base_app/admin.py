from django.contrib import admin
from .models import CategoryDish, Dish, Reservation, Event, Gallery, Chief, Reviews, Contact

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'ingredients', 'price', 'image', 'description', 'dish_order', 'is_visibility', 'is_special']
    list_filter = ['category', 'dish_order', ]
    list_editable = ['price', 'dish_order']

@admin.register(CategoryDish)
class CategoryDish(admin.ModelAdmin):
    list_display = ['name', 'is_visibility', 'position']
    list_display_links = ['position', ]

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date', 'time', 'count_people', 'message', 'is_processed']
    list_filter = ['date', 'time', ]
    list_editable = ['is_processed', ]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'upload', 'is_processed']
    list_filter = ['upload',]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'price', 'description', 'list1', 'list2', 'list3', 'description2', 'position',]
    list_filter = ['position',]
    list_editable = ['position', ]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['num', 'image',]
    list_filter = ['num',]


@admin.register(Chief)
class ChiefAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'post', 'image', 'twitter', 'facebook', 'instagram']
    list_filter = ['post',]
    list_editable = ['post', 'image', 'twitter', 'facebook', 'instagram']

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'rating', 'review', 'upload']
    list_filter = ['upload',]
    list_editable = ['rating', 'review',]



