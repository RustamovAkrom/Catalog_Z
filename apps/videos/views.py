from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Video, Tag



def videos_page(request):
    videos = Video.objects.all()

    page = request.GET.get("page", 1)
    size = request.GET.get("size", 8)
    search_value = request.GET.get("search", None)

    pagination = Paginator(videos, size)
    page_obj = pagination.get_page(page)

    if search_value is not None:
        page_obj = Video.objects.filter(title__icontains = search_value)
    else:
        search_value = ""
        
    return render(request, "videos.html", {
        "page_obj": page_obj,
        "search_value": search_value
    })


def video_detail_page(request, pk: int):
    videos = Video.objects.all()
    video = Video.objects.get(pk = pk)

    search_value = request.GET.get("search", None)

    if search_value is not None:
        
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 8)

        videos = Video.objects.filter(title__icontains = search_value)
        
        paginator = Paginator(videos, size)
        page_obj = paginator.get_page(page)

        return render(request, "videos.html", {
            "page_obj": page_obj,
            "search_value": search_value
        })
    else:
        search_value = ""

    return render(request, "video-detail.html", {
        "videos": videos,
        "video": video,
        "search_value": search_value
    })
