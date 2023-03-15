from rest_framework import status
from tests.test_setup import TestSetup
from sentry.company.models import Company
from tests.sentry.factories.company.company_factories import CompanyFactory

class SignUpTestCase(TestSetup):

    url = '/registration/signup/'

    def test_signup(self):
        pass