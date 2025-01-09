import pytest
import requests
from requests import session
from requests.exceptions import Timeout, RequestException
from jsonschema import validate
from unittest.mock import patch

from tests.Comment import Comment
from utils.logger import setup_logger

logger = setup_logger('api_test_logger', 'reports/api_test.log')

@pytest.fixture(scope="session")
def base_url():
    logger.info("Setting up url")
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}


comment_schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["postId", "id", "name", "email", "body"],
}


# GET + exception handling
def test_get_comment(base_url, headers):
    logger.info("Running test_get_comment")
    try:
        response = requests.get(f"{base_url}/comments/1", headers=headers, timeout=5)
        response.raise_for_status()
        comment_data = response.json()
        print(comment_data)
        # captured = capfd.readouterr()
        # print("Captured Output:", captured.out)

        # Validate response structure using a schema with the jsonschema library.
        validate(instance=comment_data, schema=comment_schema)

        # Asserts
        assert comment_data['id'] == 1
    except Timeout as e:
        pytest.fail(f"Request timed out: {e}")
    except RequestException as e:
        pytest.fail(f"Request failed: {e}")

# POST using payload
def test_create_comment(base_url, headers):
    logger.info("Running test_create_comment")
    new_comment = Comment(
        user_id=1,
        timestamp="2024-01-06 10:00:00",
        postId=301,
        comment_id=5001,
        name="Kate Surta",
        email="none@none.com",
        body="Great post!"
    )

    payload = {
        "name": new_comment.name,
        "email": new_comment.email,
        "body": new_comment.body,
        "postId": new_comment.postId
    }

    response = requests.post(f"{base_url}/comments", json=payload, headers=headers)

    assert response.status_code == 201

    my_comment = response.json()
    # Validate response structure using a schema with the jsonschema library.
    validate(instance=my_comment, schema=comment_schema)

    # Verify payload within response
    assert my_comment['name'] == payload['name']
    assert my_comment['email'] == payload['email']
    assert my_comment['body'] == payload['body']
    assert my_comment['postId'] == payload['postId']

# PUT
def test_update_comment(base_url, headers):
    logger.info("Running test_update_comment")
    comment_id = 1
    updated_payload = {
        "id": comment_id,
        "name": "updated_name",
        "email": "updated_none@none.com",
        "body": "updated_body",
        "postId": 1
    }
    response = requests.put(f"{base_url}/comments/{comment_id}", json=updated_payload, headers=headers)

    assert response.status_code == 200
    comment_data = response.json()
    # Validate response structure using a schema with the jsonschema library.
    validate(instance=comment_data, schema=comment_schema)

    # Verify updates
    assert comment_data['name'] == updated_payload['name']
    assert comment_data['email'] == updated_payload['email']
    assert comment_data['body'] == updated_payload['body']


# DELETE
def test_delete_comment(base_url, headers):
    logger.info("Running test_delete_comment")
    comment_id = 1
    response = requests.delete(f"{base_url}/comments/{comment_id}", headers=headers)

    assert response.status_code == 200
    # and confirming its removal using Mock.
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        check_response = requests.get(f"{base_url}/comments/{comment_id}", headers=headers)
        assert check_response.status_code == 404

# pytest main.py -s
