
"""
Perform classification via classificationbox.

For more details about this code, please refer to the documentation at
tbd
"""
import requests
import shutil

from machinebox.core import (
    check_box_health, post_file, teach_file, valid_image_file
)

from machinebox.const import (
    BOUNDING_BOX, CONFIDENCE, FILE_PATH, IMAGE_ID, ID, MATCHED, MODEL_ID, 
    MODEL_NAME, NAME, HTTP_BAD_REQUEST, HTTP_OK, HTTP_UNAUTHORIZED
)

CLASSIFIER = 'classificationbox'


def get_matched_classes(classes):
    """Return the id and score of matched classes."""
    return {class_[ID]: class_[CONFIDENCE] for class_ in classes}


def get_models(url, username, password):
    """Return the list of models."""
    kwargs = {}
    if username:
        kwargs['auth'] = requests.auth.HTTPBasicAuth(username, password)

    response = requests.get(url, **kwargs)
    response_json = response.json()
    if response_json['success']:
        return response_json['models']


def parse_classes(api_classes):
    """Parse the API classes data into the format required, a list of dict."""
    parsed_classes = []
    for entry in api_classes:
        class_ = {}
        class_[ID] = entry['id']
        class_[CONFIDENCE] = round(entry['score'] * 100.0, 2)
        parsed_classes.append(class_)
    return parsed_classes


class Classificationbox():
    """Encapsulate a Classificationbox Box."""

    def __init__(self, ip_address='localhost', port=8080, 
                 username=None, password=None, print_info=True):
        """Init with the API key and model id."""
        self._url_check = f"http://{ip_address}:{port}/{CLASSIFIER}/check"
        self._url_models = f"http://{ip_address}:{port}/{CLASSIFIER}/models"
        self._url_state = f"http://{ip_address}:{port}/{CLASSIFIER}/state"
        self._url_teach = f"http://{ip_address}:{port}/{CLASSIFIER}/teach"
        self._username = username
        self._password = password
        self._print_info = print_info # Print messages

        url_health = f"http://{ip_address}:{port}/healthz"
        self._hostname = check_box_health(
            url_health, self._username, self._password)
        
        self._models = get_models(
            self._url_models, self._username, self._password)

    @property
    def models(self):
        """Return the models information."""
        return self._models
