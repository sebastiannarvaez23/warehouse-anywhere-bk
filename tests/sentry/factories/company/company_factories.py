from faker import Faker
from sentry.company.models import Company

faker = Faker()

class CompanyFactory:

    domain = 'tenant1.localhost'

    def build_company_JSON(self):
        return {
            'schema_name': self.domain,
            'nit': str(faker.random_number(digits=10)),
            'name': faker.company(),
            'address': faker.address(),
            'country': faker.country(),
            'state': faker.state(),
            'city': faker.city()
        }
    
    def create_company(self):
        return Company.objects.create(**self.build_company_JSON())
