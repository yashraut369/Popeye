import pytest
from freelancing import FreelancingManager

def test_manage_tasks(mocker):
    mock_requests = mocker.patch('freelancing.requests')
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"jobs": [{"id": "1", "title": "Python Developer"}]}
    mock_requests.get.return_value = mock_response

    manager = FreelancingManager()
    manager.manage_tasks()

    mock_requests.get.assert_called_once