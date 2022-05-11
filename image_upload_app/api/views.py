from email.mime import image
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


@api_view(["POST"])
def upload_image(req):

    image_file = req.data.get("file")

    # Validate file as Image
    if image_file.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
        return Response({"success": False, "error": "Invalid file"}, 400)

    # Upload Request to cloudinary 3rd party service
    cloudinary_response = requests.post(
        "https://api.cloudinary.com/v1_1/"
        + env("CLOUDINARY_CLOUD_NAME")
        + "/image/upload",
        data={"upload_preset": env("CLOUDINARY_UPLOAD_RESET")},
        files={"file": image_file},
    )

    print(cloudinary_response.status_code)
    # Validate response from cloudinary 3rd party service
    if cloudinary_response.status_code != 200:
        return Response(
            {"success": False, "error": "Invalid cloudinary credentials"}, 400
        )

    cloudinary_data = cloudinary_response.json()
    return Response({"success": True, "image_link": cloudinary_data["url"]}, 200)
