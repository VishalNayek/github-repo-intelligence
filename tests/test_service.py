from service import RepositoryService
from unittest.mock import Mock

github_client = Mock()

github_client.get_repo.return_value = {
    "name": "task-manager",
    "language": "Python"
}

service = RepositoryService(github_client)

def test_get_repository_success():

    result = service.get_repository(
        "VishalNayek",
        "task-manager"
    )

    assert result == {
        "name": "task-manager",
        "language": "Python"
    }
