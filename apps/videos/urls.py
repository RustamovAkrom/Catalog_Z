from django.urls import path
from .views import videos_page, video_detail_page

app_name = "videos"
urlpatterns = [
    path("", videos_page, name="home"),
    path("videos/detail/<int:pk>", video_detail_page, name="detail")
]