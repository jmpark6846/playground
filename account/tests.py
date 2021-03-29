from rest_framework.test import APITestCase, APIClient
from account.models import User


class AuthenticationTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        data = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'test12#$',
            'password2': 'test12#$',
        }
        cls.data = data

    def test_registration_회원가입(self):
        response = self.client.post('/api/rest-auth/registration/', data=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)
        token = response.data['token']

        new_client = APIClient()
        new_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = new_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_login_로그인(self):
        User.objects.create_user(
            email=self.data['email'],
            username=self.data['username'],
            password=self.data['password1'],
        )
        login_data = {
            'username': self.data['username'],
            'password': self.data['password1']
        }
        response = self.client.post('/api/rest-auth/login/', data=login_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        token = response.data['token']

        new_client = APIClient()
        response = new_client.get('/api/users/')
        self.assertEqual(response.status_code, 401)

        new_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = new_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

