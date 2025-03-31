from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from dogs.models import Breed, Dog
from dogs.forms import DogForms


def index_view(request):
    context = {
        'objects_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главное'
    }

    return render(request, 'dogs/index.html', context=context)


def breeds_list_view(request):
    context = {
        'objects_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context=context)


def breed_dogs_list_view(request, pk: int):
    breed_object = Breed.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - {breed_object.name}',
        'breed_pk': breed_object.pk
    }
    return render(request, 'dogs/dogs.html', context=context)


def dogs_list_view(request):
    context = {
        'objects_list': Dog.objects.all(),
        'title': f'Все наши собаки',
    }
    return render(request, 'dogs/dogs.html', context=context)


# Create Read Update Delete (CRUD)
def dog_create_view(request):
    if request.method == 'POST':
        form = DogForms(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'title': 'Добавить собаку',
        'form': DogForms
    }
    return render(request, 'dogs/create.html', context=context)
    # return render(request, 'dogs/create.html', {'form': DogForms})   пример без context
