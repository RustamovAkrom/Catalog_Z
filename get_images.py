import os
import django
import requests
from io import BytesIO
from django.core.files import File

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.photos.models import Photo

def get_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:

        # Create a temporary file
        image_name = os.path.basename(image_url)
        temp_file = BytesIO(response.content)
        temp_file.seek(0)
        return image_name, temp_file
    else:
        print(f"Failed to download image: {image_url}")


def add_photo():
    
    photo = Photo()
    photo.title = input("title: ")

    image_name, temp_file = get_image(input("image url: "))
    photo.photo.save(image_name, File(temp_file), save=True)

    photo.format = input("format: ")
    photo.dimension = input("dimension: ")
    photo.license = input("license: ")
    photo.tags.set([int(input('tag id: '))])

    photo.save()
    print(f"Image <{photo.title}> saved successfully.")

    
def main():
    add_photo()

if __name__ == "__main__":
    main()