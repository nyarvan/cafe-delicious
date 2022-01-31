from django.shortcuts import render, redirect
from base_app.models import Reservation, Contact, CategoryDish, Dish
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .forms import FormDishs, FormCategoryDishs

def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations_list(request):
    reservation = Reservation.objects.filter(is_processed=False).order_by('-date')

    paginator = Paginator(reservation, 5)
    page = request.GET.get('page')

    reservation = paginator.get_page(page)
    return render(request, 'reservation_list.html', context={'reg_list': reservation})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('reservations_list')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_list(request):
    contact = Contact.objects.filter(is_processed=False).order_by('-upload')

    paginator = Paginator(contact, 5)
    page = request.GET.get('page')

    contact = paginator.get_page(page)
    return render(request, 'contact_list.html', context={'contact_list': contact})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_contact(request, pk):
    Contact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('contact_list')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def main_menu_list(request):
    category = CategoryDish.objects.all().order_by('position')
    dishs = Dish.objects.filter(is_special=False).order_by('category')
    special = Dish.objects.filter(is_special=True).order_by('category')

    paginator = Paginator(dishs, 5)
    paginator2 = Paginator(special, 5)
    page = request.GET.get('page')

    dishs = paginator.get_page(page)
    special = paginator2.get_page(page)
    return render(request, 'main_menu_list.html', context={'categories': category, 'dishs': dishs, 'special': special})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def add_dish(request):
    if request.method == 'POST':
        form_dish = FormDishs(request.POST, request.FILES)
        if form_dish.is_valid():
            form_dish.save()
            return redirect('main_menu_list')

    form_dish = FormDishs()
    return render(request, 'form_add_dish.html', context={
        'form_dish': form_dish,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def add_category(request):
    if request.method == "POST":
        form_category = FormCategoryDishs(request.POST)
        if form_category.is_valid():
            form_category.save()
            return redirect('main_menu_list')

    form_category = FormCategoryDishs()
    return render(request, 'form_add_category.html', context={'form_category': form_category})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def add_special(request):
    if request.method == "POST":
        form_special = FormDishs(request.POST, request.FILES)
        if form_special.is_valid():
            form_special.save()
            return redirect('main_menu_list')

    form_special = FormDishs()
    return render(request, 'form_add_special.html', context={'form_dish': form_special})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_dish(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        dish.title = request.POST.get("title")
        dish.ingredients = request.POST.get("ingredients")
        dish.price = request.POST.get("price")
        dish.image = request.FILES.get("image")
        dish.description = request.POST.get("description")
        dish.dish_order = request.POST.get("dish_order")
        dish.is_visibility = request.POST.get("is_visibility")
        dish.is_special = request.POST.get("is_special")
        dish.save()
        return redirect("main_menu_list")

    form_dish = FormDishs()
    category = CategoryDish.objects.all()
    return render(request, 'form_update_dish.html', context={
        "form_dish": form_dish,
        "dish": dish,
        "category": category,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_category(request, pk):
    category = CategoryDish.objects.get(pk=pk)
    if request.method == "POST":
        category.name = request.POST.get("name")
        category.position = request.POST.get("position")
        category.save()
        return redirect('main_menu_list')

    return render(request, 'form_update_category.html', context={'category': category})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def delete_dish(request, pk):
    dish = Dish.objects.get(pk=pk)
    dish.delete()
    return redirect("main_menu_list")

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def delete_category(request, pk):
    category = CategoryDish.objects.get(pk=pk)
    category.delete()
    return redirect("main_menu_list")

