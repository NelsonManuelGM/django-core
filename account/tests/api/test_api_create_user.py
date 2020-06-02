"""Create user test module"""
import json

from django.urls import reverse
from django.utils.encoding import force_str
from rest_framework import status

from appcore.tests.test_core import APITestCaseCore


class CreateUserTestCase(APITestCaseCore):
    """Test class for user API"""

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('api_account_users-list')

    def test_create_user(self):
        """test to create user"""
        data = self.create_fake_user()
        str_json_data = json.dumps(data)

        response = self.client.post(self.url, data=str_json_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        api_response = json.loads(force_str(response.content))

        self.assertEqual(api_response['first_name'],
                         data['first_name'])

        self.assertEqual(api_response['last_name'],
                         data['last_name'])
