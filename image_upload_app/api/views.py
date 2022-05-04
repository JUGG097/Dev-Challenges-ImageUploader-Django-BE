from email.mime import image
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests


@api_view(["POST"])
def upload_image(req):
    try:
        image_file = req.data.get("file")

        print(req.data)
        # Validate file as Image
        if image_file.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
            return Response({"success": False, "message": "Invalid file"}, 400)

        # Upload Request to cloudinary 3rd party service
        cloudinary_response = requests.post(
            "https://api.cloudinary.com/v1_1/dcym0jsal/image/upload",
            data={"upload_preset": "dev-challenges"},
            files={"file": image_file},
        )

        print(cloudinary_response.status_code)
        # Validate response from cloudinary 3rd party service
        if cloudinary_response.status_code != 200:
            return Response(
                {"success": False, "message": "Invalid cloudinary credentials"}, 400
            )

        cloudinary_data = cloudinary_response.json()
        return Response({"success": True, "image_link": cloudinary_data["url"]}, 200)
    except:
        return Response({"success": False, "message": "System Error: Unknown"}, 500)
