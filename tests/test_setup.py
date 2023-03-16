from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

faker = Faker()

class TestSetup(APITestCase):
    def setUp(self):
        """Test that allows testing the registration and login of a user"""
        from sentry.registration.models import User, Rol
        from sentry.company.models import Company

        self.login_url = '/registration/login/'
        
        company = Company.objects.create(nit='1234', name='companytest', domain='co', address='co', country=faker.country(), region=faker.state(), city=faker.city())
        self.user = User.objects.create_superuser(
            username=faker.name(),
            email=faker.email(),
            first_name='First Name',
            last_name='Last Name',
            telephone='12345',
            company=company.id,
            password='Manage123'
        )

        response = self.client.post(
            self.login_url,
            {
                'username': self.user.username,
                'password': 'Manage123'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        return super().setUp()