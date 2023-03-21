from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

faker = Faker()

class TestSetup(APITestCase):
    def setUp(self):
        pass