from faker import Faker
from saleorder.models import SaleOrder, PayTerm, Collection

faker = Faker()

class SaleOrderItemFactory:

    def build