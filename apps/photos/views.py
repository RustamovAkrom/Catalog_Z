from django.shortcuts import render, redirect
from .models import Photo, Tag
from .forms import ContactForm


def photos_page(request):
    photos = Photo.objects.all()
    print(photos)
    return render(request, "index.html", {
        "photos": photos
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
            return redirect("photos:contact")
    form = ContactForm()
    return render(request, "contact.html", {
        "form": form
    })


def about_page(request):
    return render(request, "about.html")