from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.photos.models import Tag, Photo


class PhotosTestCase(TestCase):

    def test_get_home(self):
        response = self.client.get(reverse("photos:home"))
        self.assertEqual(response.status_code, 200)

    # def test_get_photo(self):
    #     tag = Tag.objects.create(name = "tag1")
    #     photo = Photo.objects.create(
    #         title = "title1",
    #         photo = SimpleUploadedFile(name="logo.jpg", content=b"", content_type="image/jpeg"),
    #         format = "JPG",
    #         dimension = "sldjflal",
    #         license = "license1",
    #     )
    #     photo.tags.set([tag])
    #     response = self.client.get(reverse("photos:detail", kwargs={"pk": 1}))
    #     print(response.json())
    #     print(response.status_code)
        

    def test_get_contact(self):
        response = self.client.get(reverse("photos:contact"))
        self.assertEqual(response.status_code, 200)

    def test_get_about(self):
        response = self.client.get(reverse("photos:about"))
        self.assertEqual(response.status_code, 200)