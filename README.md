# Image Uploader Django Backend Project (The backend for the Image Uploader Website deployed [here](https://imageuploader-adeoluwa.netlify.app/).)

This project was developed using `Python` v "^3.9", `Django` v "^4.0.4", `Requests` v "^2.27.1", `Sentry-sdk` v "^1.5.11", and `Djangorestframework` v "^3.13.1" libraries.

Deployed on a `Digital Oceans` Droplet using `Github Actions` for CI/CD.

The Image Uploader Website was deployed with `Netlify` link [here](https://imageuploader-adeoluwa.netlify.app/).

Figma design was provided by [devChallenges.io](https://devchallenges.io/).

You can clone project and customise at your end.

### API Documentation

- 'http://127.0.0.1:8000/v1/image/' Endpoint

METHOD: 'POST'

BODY: {'file': Image File}

SUCCESS RESPONSE (200): {'success': true, 'image_link': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'error': '***********'}
