from faker import Faker
from sentry.company.models import Company, Country, City

faker = Faker()

class CompanyFactory:

    def build_country_JSON(self):
        return {
            'code': faker.country_code(),
            'name': faker.country()
        }
    
    def build_city_JSON(self):
        country_obj = self.create_country()
        return {
            'name': faker.city(),
            'country': country_obj
        }

    def build_company_JSON(self):
        city_obj = self.create_city()
        return {
            'nit': str(faker.random_number(digits=10)),
            'name': faker.company(),
            'domain': faker.domain_name(),
            'address': faker.address(),
            'city': city_obj
        }
    
    def create_country(self):
        return Country.objects.create(**self.build_country_JSON())
    
    def create_city(self):
        return City.objects.create(**self.build_city_JSON)
    
    def create_company(self):
        return Company.objects.create(**self.build_company_JSON())
