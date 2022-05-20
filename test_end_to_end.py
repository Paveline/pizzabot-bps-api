import pytest

from app import app
from flask import json


def test__pizzabot_end_with_status_200():
    response = app.test_client().post(
        '/pizzabot',
        data=json.dumps({'pizzabot': "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['instructions'] == 'DNNNEDNEEEDSSDDSWWWWDNEEEDNWDSSEED'
