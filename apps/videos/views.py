from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Video, Tag



def videos_page(request):
    videos = Video.objects.all()

    page = request.GET.get("page", 1)
    size = request.GET.get("size", 8)

    pagination = Paginator(videos, size)
    page_obj = pagination.get_page(page)

    return render(request, "videos.html", {
        "page_obj": page_obj
    })


def video_detail_page(request, pk: int):
    videos = Video.objects.all()
    video = Video.objects.get(pk = pk)

    return render(request, "video-detail.html", {
        "videos": videos,
        "video": video
    })
