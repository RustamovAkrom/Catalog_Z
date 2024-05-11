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
    format = models.CharField(max_length=3)
    dimension = models.CharField(max_length=9)
    license = models.CharField(max_length=180)
    tags = models.ManyToManyField(Tag, related_name="photos")
    
    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = "photos"

    def __str__(self) -> str:
        return self.title
    

class Contact(AbstractBaseModel):
    SUBJECT_LIST_SELECTOR = [
        ("subject", "Subject"),
        ("sales_marketing", "Sales & Marketing"),
        ("create_design", "Create Design"),
        ("ui_ux", "UI / UX"),
    ]
    name = models.CharField(max_length=28)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=16, choices = SUBJECT_LIST_SELECTOR)
    message = models.TextField()

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"