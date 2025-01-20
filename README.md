# Image Uploader Django Backend Project (The backend for the Image Uploader Website code [here](https://github.com/JUGG097/Dev-Challenges-ImageUploader-React-FE).)

This project was developed using `Python` v "^3.9", `Django` v "^4.0.4", `Requests` v "^2.27.1", `Sentry-sdk` v "^1.5.11", and `Djangorestframework` v "^3.13.1" libraries.

Deployed on a `Digital Oceans` Droplet using `Github Actions` for CI/CD.

The Image Uploader Website can be deployed with `Netlify`.

Figma design was provided by [devChallenges.io](https://devchallenges.io/).

You can clone project and customise at your end.

### API Documentation

- 'http://127.0.0.1:8000/v1/image/' Endpoint

METHOD: 'POST'

BODY: {'file': Image File}

SUCCESS RESPONSE (200): {'success': true, 'image_link': '**********'}

ERROR RESPONSE (4**, 5**): {'success': false, 'error': '***********'}
