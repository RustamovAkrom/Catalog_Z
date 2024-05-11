from django.shortcuts import render
from .models import Video, Tag



def videos_page(request):
    videos = Video.objects.all()

    return render(request, "videos.html", {
        "videos": videos
    })


def video_detail_page(request, pk: int):
    videos = Video.objects.all()
    video = Video.objects.get(pk = pk)

    return render(request, "video-detail.html", {
        "videos": videos,
        "video": video
    })
