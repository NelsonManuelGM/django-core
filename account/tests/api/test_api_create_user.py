"""Create user test module"""
import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import force_str
from rest_framework import status

from appcore.tests.test_core import APITestCaseCore


class CreateUserTestCase(APITestCaseCore):
    """Test class for user API"""

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('api_account_users-list')

    def test_list_user(self):
        """test get user function"""

        quantity = 10
        users = []
        for i in range(quantity):
            # pylint: disable=no-value-for-parameter
            user1_data = self.generate_fake_user_dict()
            user_obj = get_user_model()()
            user_obj.fill(user1_data)
            user_obj.save()
            users.append(user_obj)

        response = self.client.get(self.url,
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json_data = json.loads(response.content)

        results = json_data['results']

        for i in range(quantity):
            self.assertEqual(users[i].first_name, results[i]['first_name'])

        self.assertEqual(json_data['count'], quantity)

    def test_create_user(self):
        """test to create user"""
        # pylint: disable=no-value-for-parameter
        data = self.generate_fake_user_dict()
        str_json_data = json.dumps(data)

        response = self.client.post(self.url, data=str_json_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        api_response = json.loads(force_str(response.content))

        self.assertEqual(api_response['first_name'],
                         data['first_name'])

        self.assertEqual(api_response['last_name'],
                         data['last_name'])
