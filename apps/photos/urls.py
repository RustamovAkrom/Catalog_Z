from django.urls import path
from .views import photos_page, photos_detail_page, contact_page, about_page

app_name = "photos"

urlpatterns = [
    path('', photos_page, name='home'),
    path('photo/<int:pk>', photos_detail_page, name="detail"),
    path('contact/', contact_page, name="contact"),
    path('about/', about_page, name="about"),
]