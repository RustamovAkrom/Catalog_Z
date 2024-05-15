from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from celery import shared_task
from .models import Photo, Tag
from .forms import ContactForm


def photos_page(request):
    photos = Photo.objects.all()

    page = request.GET.get("page", 1)
    size = request.GET.get("size", 8)
    search_value = request.GET.get('search', None)

    paginator = Paginator(photos, size)

    page_obj = paginator.get_page(page)

    if search_value is not None:
        page_obj = Photo.objects.filter(title__icontains = search_value)
    else:
        search_value = ""
        
    return render(request, "index.html", {
        "page_obj": page_obj,
        "search_value": search_value
    })


def photos_detail_page(request, pk: int):
    photos = Photo.objects.all()
    photo = Photo.objects.get(pk = pk)

    search_value = request.GET.get("search", None)

    if search_value is not None:
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 8)

        photos = Photo.objects.filter(title__icontains = search_value)

        paginator = Paginator(photos, size)
        
        page_obj = paginator.get_page(page)

        return render(request, "index.html", {
            "page_obj": page_obj,
            "search_value": search_value
        })

    return render(request, "photo-detail.html", {
        "photos":photos,
        "photo": photo
    })


@shared_task
def contact_page(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("photos:home")
        else:
            return redirect("photos:conact")
        
    form = ContactForm()
    return render(request, "contact.html", {
        "form": form
    })


def about_page(request):
    return render(request, "about.html")