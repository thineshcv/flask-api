import pytest
from unittest.mock import patch, mock_open
from flask import Flask
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import get_json

# Test the get_json function
def test_get_json():
    with patch('builtins.open', mock_open(read_data='{"key": "value"}')) as mock_file:
        app = Flask(__name__)
        app.route('/data/<filename>', methods=['GET'])(get_json)

        with app.test_client() as client:
            response = client.get('/data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json')
            assert response.status_code == 200
            assert response.get_json() == {'key': 'value'}

if __name__ == '__main__':
    pytest.main()
