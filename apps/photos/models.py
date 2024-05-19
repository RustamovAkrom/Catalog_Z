from apps.shared.models import AbstractBaseModel
from django.db import models



class Tag(AbstractBaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = "tags"

    def __str__(self) -> str:
        return self.name
    

class Photo(AbstractBaseModel):
    title = models.CharField(max_length=80)
    photo = models.ImageField(upload_to="photos/")
    format = models.CharField(max_length=4)
    dimension = models.CharField(max_length=9)
    license = models.CharField(max_length=180)
    tags = models.ManyToManyField(Tag, related_name="photos")
    
    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = "photos"

    def __str__(self) -> str:
        return self.title
    
