import unittest
from unittest.mock import patch, MagicMock
from mock_practice import len_joke, get_joke

class TestgetJoke(unittest.TestCase):

    @patch('mock_practice.get_joke')
    def test_len_joke(self,mock_obj):
        mock_obj.return_value = "hardcoded_value"
        self.assertEqual(len_joke(), 15)

    @patch('mock_practice.requests.get')
    def test_get_joke_if(self, mock_obj):

        mock_obj.return_value = MagicMock()
        mock_obj.return_value.status_code = 200
        mock_obj.return_value.json.return_value = {'value':{'joke':2}}
        self.assertEqual(get_joke(),2)

    #OR
    @patch('mock_practice.requests')
    def test_get_joke_2ns_approch(self, mock_obj):

        # mock_response = MagicMock()
        # mock_response.status_code = 200
                #OR
        mock_response = MagicMock(status_code = 200)
        mock_response.json.return_value = {'value':{'joke':1111}}
        mock_obj.get.return_value = mock_response
        self.assertEqual(get_joke(),1111)

    

    @patch('mock_practice.requests.get')
    def test_get_joke_else(self, mock_obj):
        mock_obj.return_value = MagicMock()
        mock_obj.return_value.status_code = 100
        self.assertEqual(get_joke(), "No joke")


