"""The tests for the facebox component."""
from unittest.mock import Mock, mock_open, patch

import pytest
import requests
import requests_mock

from machinebox.core import check_box_health
from machinebox.const import (
    NAME, IMAGE_ID, CONFIDENCE, MATCHED, BOUNDING_BOX, 
    HTTP_OK, HTTP_UNAUTHORIZED
)

MOCK_IP = '192.168.0.1'
MOCK_PORT = '8080'

# Mock data returned by the facebox API.
MOCK_BOX_ID = 'b893cc4f7fd6'
MOCK_ERROR_NO_FACE = "No face found"
MOCK_FACE = {'confidence': 0.5812028911604818,
             'id': 'john.jpg',
             'matched': True,
             'name': 'John Lennon',
             'rect': {'height': 75, 'left': 63, 'top': 262, 'width': 74}}

MOCK_FILE_PATH = '/images/mock.jpg'

MOCK_HEALTH = {'success': True,
               'hostname': 'b893cc4f7fd6',
               'metadata': {'boxname': 'facebox', 'build': 'development'},
               'errors': []}

MOCK_JSON = {"facesCount": 1,
             "success": True,
             "faces": [MOCK_FACE]}

MOCK_NAME = 'mock_name'
MOCK_USERNAME = 'mock_username'
MOCK_PASSWORD = 'mock_password'

# Faces data after parsing.
PARSED_FACES = [{NAME: 'John Lennon',
                 IMAGE_ID: 'john.jpg',
                 CONFIDENCE: 58.12,
                 MATCHED: True,
                 BOUNDING_BOX: {
                     'height': 75,
                     'left': 63,
                     'top': 262,
                     'width': 74}}]

MATCHED_FACES = {'John Lennon': 58.12}


@pytest.fixture
def mock_healthybox():
    """Mock check_box_health."""
    with patch('machinebox.core.check_box_health', return_value=MOCK_BOX_ID) as _mock_healthybox:
        yield _mock_healthybox


def test_check_box_health(caplog):
    """Test check box health."""
    with requests_mock.Mocker() as mock_req:
        url = "http://{}:{}/healthz".format(MOCK_IP, MOCK_PORT)
        mock_req.get(url, status_code=HTTP_OK, json=MOCK_HEALTH)
        assert check_box_health(url, 'user', 'pass') == MOCK_BOX_ID

        mock_req.get(url, status_code=HTTP_UNAUTHORIZED)
        assert check_box_health(url, None, None) is None

