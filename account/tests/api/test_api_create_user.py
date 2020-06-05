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
        # pylint: disable=no-value-for-parameter
        user1_data = self.generate_fake_user_dict()
        user_obj_1 = get_user_model()()
        user_obj_1.fill(user1_data)
        user_obj_1.save()

        # pylint: disable=no-value-for-parameter
        user2_data = self.generate_fake_user_dict()
        user_obj_2 = get_user_model()()
        user_obj_2.fill(user2_data)
        user_obj_2.save()

        response = self.client.get(self.url,
                                   content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        json.loads(force_str(response.content))

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
