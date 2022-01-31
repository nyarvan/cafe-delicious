from django.shortcuts import render, redirect
from .models import Dish, CategoryDish, Event, Gallery, Chief, Reviews
from .form import FormReservation, FormContact, FormReview

def base_app_view(request):
    if request.method == 'POST':
        form_reservation = FormReservation(request.POST)
        form_contact = FormContact(request.POST)
        if form_reservation.is_valid():
            form_reservation.save()
            return redirect('/')
        elif form_contact.is_valid():
            form_contact.save()
            return redirect('/')

    form_reservation = FormReservation()
    form_contact = FormContact()
    dishes = Dish.objects.filter(is_visibility=True, is_special=False).order_by('dish_order')
    categories = CategoryDish.objects.filter(is_visibility=True).order_by('position')
    special = Dish.objects.filter(is_visibility=True, is_special=True).order_by('dish_order')
    events = Event.objects.filter().order_by('position')
    gallery = Gallery.objects.order_by('?')[:8]
    chiefs = Chief.objects.order_by('?')[:3]
    reviews = Reviews.objects.order_by('?')[:6]
    return render(request, 'base_app.html', context={
        'dishes': dishes,
        'categories': categories,
        'special': special,
        'form_reservation': form_reservation,
        'form_contact': form_contact,
        'events': events,
        'gallery': gallery,
        'chiefs': chiefs,
        'reviews': reviews,
    })

def add_review(request):
    if request.method == 'POST':
        form_review = FormReview(request.POST, request.FILES)
        if form_review.is_valid():
            form_review.save()
            return redirect('base_app:base_app_view')

    form_review = FormReview()
    return render(request, 'add_review.html', context={"form_review": form_review})



