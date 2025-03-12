import pytest
from unittest.mock import patch, MagicMock
from webscrappy.mainScrappy import download_pages

@pytest.fixture
def mock_event():
    return {}

@pytest.fixture
def mock_context():
    return {}

@patch("webscrappy.mainScrappy.s3")
@patch("webscrappy.mainScrappy.requests.Session")
def test_download_ok(mock_session, mock_s3, mock_event, mock_context):
    mock_sess_instance = MagicMock()
    mock_session.return_value = mock_sess_instance
    
    mock_response = MagicMock(status_code=200, text="<html>OK</html>")
    mock_sess_instance.get.return_value = mock_response

    result = download_pages(mock_event, mock_context)

    assert result["status"] == "success"
    assert mock_sess_instance.get.call_count == 10
    assert mock_s3.put_object.call_count == 10

