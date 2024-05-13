from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Photo, Tag
from .forms import ContactForm


def photos_page(request):
    photos = Photo.objects.all()

    page = request.GET.get("page", 1)
    size = request.GET.get("size", 8)

    paginator = Paginator(photos, size)

    page_obj = paginator.get_page(page)

    return render(request, "index.html", {
        "page_obj": page_obj
    })


def photos_detail_page(request, pk: int):
    photos = Photo.objects.all()
    photo = Photo.objects.get(pk = pk)

    return render(request, "photo-detail.html", {
        "photos":photos,
        "photo": photo
    })


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