import requests
from app.settings import API_LOG_NAME
from django.test import TestCase
from unittest.mock import patch, MagicMock
from .utils import RequestHandler
from requests.models import Response


class BadRequestTest(TestCase):
    @patch("requests.adapters.HTTPAdapter.send")
    def test_get_request(self, mock_get):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 400
        mock_response.content.decode.return_value = '{"detail": "Bad Request!"}'
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_get.return_value = mock_response
        
        req = RequestHandler()
        
        with self.assertLogs(API_LOG_NAME, level='ERROR') as log_cm:
            res = req.get("http://api:10001/test/api/500/server_error")
            print(res.status_code)
            print(res.content)
            
            # Debug output
            print(log_cm.output)

            # Assert that logger.error was called with the expected message
            self.assertTrue(any("Bad Request" in message for message in log_cm.output))

        # Assert that response is None
        self.assertIsNone(res)