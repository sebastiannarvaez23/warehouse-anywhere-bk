from faker import Faker
from saleorder.models import SaleOrder, PayTerm, Collection

faker = Faker()

class SaleOrderFactory:

    def build_pay_term_JSON(self):
        pay_term_list = ['Contado', '30 días', '45 días']
        return {
            'name': faker.random_element(elements=pay_term_list)
        }
    
    def build_collection_JSON(self):
        return {
            'name': faker.sentence(nb_words=3)
        }

    def build_sale_order_JSON(self):
        pay_term_obj = self.create_pay_term()
        collection_obj = self.create_collection()
        return {
            'no_sale_order': str(faker.random_number(digits=4)),
            'publication_date': faker.date_this_decade(),
            'delivery_date': faker.date_this_decade(),
            'doc_date': faker.date_this_decade(),
            'doc_date': faker.date_this_decade(),
            'po_comments': faker.text(max_nb_chars=500),
            'customer_name': faker.name(),
            'delivery_address': faker.address(),
            'pay_term': pay_term_obj,
            'collection': collection_obj
        }

    def create_sale_order(self):
        return SaleOrder.objects.create(**self.build_sale_order_JSON())
    
    def create_pay_term(self):
        return PayTerm.objects.create(**self.build_pay_term_JSON())

    def create_collection(self):
        return Collection.objects.create(**self.build_collection_JSON())