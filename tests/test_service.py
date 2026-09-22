from service import RepositoryService, RepositoryNotFoundError
from unittest.mock import Mock
import requests
import pytest



def test_get_repository_success():

    github_client = Mock()

    github_client.get_repo.return_value = {
        "name": "task-manager",
        "language": "Python"
}

    service = RepositoryService(github_client)

    result = service.get_repository(
        "VishalNayek",
        "task-manager"
    )

    assert result == {
        "name": "task-manager",
        "language": "Python"
    }

def test_get_repository_not_found():

    github_client = Mock()

    error = requests.exceptions.HTTPError()

    response = Mock()
    response.status_code = 404

    error.response = response

    github_client.get_repo.side_effect = error

    service = RepositoryService(github_client)

    with pytest.raises(RepositoryNotFoundError):
        service.get_repository(
            "VishalNayek",
            "does-not-exist"
        )
