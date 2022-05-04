from django.urls import path
from image_upload_app.api.views import upload_image

urlpatterns = [
    path("image/", upload_image, name="image"),
]
