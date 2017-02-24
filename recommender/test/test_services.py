import webapp2
import json

from test_base import TestBase
from src import main

class AccessHandlerTest(TestBase):

    def test_access_handler(self):
        request = webapp2.Request.blank("/services/register")
        request.method = "POST"
        request.headers['Content-Type'] = 'application/json'
        request.body = '{"user_id": 1, "item_id": 15}'
        response = request.get_response(main.app)
        data = json.loads(response.body)

        self.assertEqual(data['status'], 200)
