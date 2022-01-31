from django.urls import path
from .views import reservations_list, update_reservation, contact_list, \
    update_contact, main_menu_list, add_dish, \
    update_dish, delete_dish, add_category, \
    update_category, delete_category, add_special

urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reservation'),
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/update/<int:pk>/', update_contact, name="update_contact"),
    path('menu/main/', main_menu_list, name="main_menu_list"),
    path('menu/main/add/', add_dish, name="add_dish"),
    path('menu/main/update/<int:pk>/', update_dish, name="update_dish"),
    path('menu/main/delete/<int:pk>/', delete_dish, name="delete_dish"),
    path('menu/category/add/', add_category, name="add_category"),
    path('menu/category/update/<int:pk>/', update_category, name="update_category"),
    path('menu/category/delete/<int:pk>/', delete_category, name="delete_category"),
    path('menu/special/add/', add_special, name="add_special"),
    path('menu/special/update/<int:pk>/', update_dish, name="update_special"),
    path('menu/special/delete/<int:pk>/', delete_dish, name="delete_special"),
]