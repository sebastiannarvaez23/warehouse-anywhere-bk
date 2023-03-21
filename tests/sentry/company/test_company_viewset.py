from rest_framework import status
from tests.test_setup import TestSetup
from sentry.company.models import Company
from tests.sentry.factories.company.company_factories import CompanyFactory

class CompanyTestCase(TestSetup):
    url = '/company/'

    def test_create_company(self):
        company = CompanyFactory().build_company_JSON()
        response = self.client.post(
            self.url,
            company,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.all().count(), 2)
        self.assertEqual(response.data['schema_name'], company['schema_name'])
        self.assertEqual(response.data['nit'], company['nit'])
        self.assertEqual(response.data['name'], company['name'])
        self.assertEqual(response.data['address'], company['address'])
        self.assertEqual(response.data['country'], company['country'])
        self.assertEqual(response.data['state'], company['state'])
        self.assertEqual(response.data['city'], company['city'])