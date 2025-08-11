from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Plant, Group, Category, Content
from .forms import PlantForm, ContentForm, GroupForm


@login_required
def plant_list(request):
    user = request.user
    name_filter = request.GET.get('name', '')
    group_filter = request.GET.get('group', '')

    plants_qs = Plant.objects.filter(owners=user)

    if name_filter:
        plants_qs = plants_qs.filter(name__icontains=name_filter)

    if group_filter:
        plants_qs = plants_qs.filter(group_id=group_filter)

    categories = Category.objects.all()
    groups = Group.objects.all()
    all_plants = Plant.objects.all()

    contents = Content.objects.filter(plant__in=plants_qs).values('plant_id', 'category_id')

    content_map = {}
    for c in contents:
        content_map.setdefault(c['plant_id'], set()).add(c['category_id'])

    plants_data = []
    for plant in plants_qs:
        category_status = {}
        for category in categories:
            category_status[category.id] = category.id in content_map.get(plant.id, set())
        plants_data.append({'plant': plant, 'category_status': category_status})

    context = {
        'plants': plants_data,
        'categories': categories,
        'groups': groups,
        'name_filter': name_filter,
        'group_filter': group_filter,
        'all_plants': all_plants,
    }
    return render(request, 'garden/plant_list.html', context)


@login_required
def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    contents = Content.objects.filter(plant=plant).select_related('category')
    return render(request, 'garden/plant_detail.html', {
        'plant': plant,
        'contents': contents
    })


@login_required
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            plant.owners.add(request.user)
            messages.success(request, "Planta adicionada com sucesso.")
            return redirect('garden:plant_list')
        else:
            messages.error(request, "Por favor corrija os erros no formulário.")
    else:
        form = PlantForm()
    return render(request, 'garden/add_plant.html', {'form': form})


@login_required
def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Conteúdo adicionado com sucesso.")
            return redirect('garden:plant_list')
        else:
            messages.error(request, "Por favor corrija os erros no formulário.")
    else:
        form = ContentForm()
    return render(request, 'garden/add_content.html', {'form': form})


@login_required
def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grupo adicionado com sucesso.")
            return redirect('garden:plant_list')
        else:
            messages.error(request, "Por favor corrija os erros no formulário.")
    else:
        form = GroupForm()
    return render(request, 'garden/add_group.html', {'form': form})


@login_required
def add_plant_to_user(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.user in plant.owners.all():
        messages.info(request, "Você já possui essa planta.")
    else:
        plant.owners.add(request.user)
        messages.success(request, "Planta adicionada à sua coleção.")
    return redirect('garden:plant_list')


@login_required
def remove_plant_from_user(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    if request.user in plant.owners.all():
        plant.owners.remove(request.user)
        messages.success(request, "Planta removida da sua coleção.")
    else:
        messages.info(request, "Você não possui essa planta.")
    return redirect('garden:plant_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso.")
            return redirect('garden:plant_list')
        else:
            messages.error(request, "Por favor corrija os erros no formulário.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@require_POST
@login_required
def logout_view(request):
    auth_logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('garden:login')
