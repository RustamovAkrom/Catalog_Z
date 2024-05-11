from django.urls import path
from .views import photos_page, photos_detail_page, contact_page, about_page

app_name = "photos"

urlpatterns = [
    path('', photos_page, name='home'),
    path('photo/detail/<int:pk>', photos_detail_page, name="detail"),
    path('photo/contacts/', contact_page, name="contact"),
    path('photos/about', about_page, name="about"),
]