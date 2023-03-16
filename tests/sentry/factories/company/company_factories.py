from faker import Faker
from sentry.company.models import Company

faker = Faker()

class CompanyFactory:

    def build_company_JSON(self):
        return {
            'nit': str(faker.random_number(digits=10)),
            'name': faker.company(),
            'domain': faker.domain_name(),
            'address': faker.address(),
            'country': faker.country(),
            'region': faker.state(),
            'city': faker.city()
        }
    
    def create_company(self):
        return Company.objects.create(**self.build_company_JSON())
