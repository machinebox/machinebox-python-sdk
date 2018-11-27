"""
Core methods for Machinebox.
"""
import requests
from PIL import Image

from machinebox.const import HTTP_OK


def check_box_health(url, username, password):
    """Check the health of the classifier and return its id if healthy."""
    kwargs = {}
    if username:
        kwargs['auth'] = requests.auth.HTTPBasicAuth(username, password)

    try:
        response = requests.get(
            url,
            **kwargs
        )
        if response.status_code == HTTP_OK:
            return response.json()['hostname']
        return None
    except Exception as exc:
        print(exc)


def post_file(url, file_path, username, password):
    """Post an image file to the classifier."""
    kwargs = {}
    if username:
        kwargs['auth'] = requests.auth.HTTPBasicAuth(username, password)
    file = {'file': open(file_path, 'rb')}

    response = requests.post(
        url,
        files=file,
        **kwargs
    )

    if response.status_code == HTTP_OK:
        return response
    return None


def teach_file(url, name, file_path, username, password):
    """Teach the classifier a name associated with a file."""
    kwargs = {}
    if username:
        kwargs['auth'] = requests.auth.HTTPBasicAuth(username, password)

    with open(file_path, 'rb') as open_file:
        response = requests.post(
            url,
            data={'name': name, 'id': file_path},
            files={'file': open_file},
            **kwargs
        )

    if response.status_code == HTTP_OK:
        return response
    return None


def valid_image_file(file_path):
    """Lazily check that a file_path points to a valid image file."""
    try:
        Image.open(file_path)
        return True
    except Exception as error:
        print(error)
        return False
