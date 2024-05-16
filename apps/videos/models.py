from apps.shared.models import AbstractBaseModel
from django.db import models


class Tag(AbstractBaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self) -> str:
        return self.name
    

class Video(AbstractBaseModel):
    title = models.CharField(max_length=80)
    video = models.FileField(upload_to="videos/")
    resolution = models.CharField(max_length=9)
    format = models.CharField(max_length=3)
    duration = models.TimeField()
    license = models.CharField(max_length=180)
    tags = models.ManyToManyField(Tag, related_name="videos")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"

    def __str__(self) -> str:
        return self.title
    

