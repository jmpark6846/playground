from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from user.models import User, UserProfile



class UserTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        data = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'test12#$',
            'password2': 'test12#$',
        }
        cls.data = data

    def test_registration_회원가입하면_유저와_프로필_생성(self):
        response = self.client.post('/api/registration/', data=self.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)

        email = response.data['user']['email']
        user = User.objects.get(email=email)
        self.assertIsNotNone(user.profile)

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
            'email': self.data['email'],
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

    def test_work_experience_유저가_경력사항을_생성_조회한다(self):
        user = User.objects.create_user(
            email=self.data['email'],
            username=self.data['username'],
            password=self.data['password1'],
        )

        client = APIClient()
        client.force_login(user)
        data = {
            'profile': user.profile.id,
            'company': 'rocketpunch',
            'start_date': timezone.now(),
            'description': 'test description'
        }
        response = client.post('/api/work_exps/', data=data)
        self.assertEqual(response.status_code, 201)

        work_exp_dict = response.data
        response = client.get(f'/api/work_exps/{work_exp_dict["id"]}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(work_exp_dict['id'], response.data['id'])

