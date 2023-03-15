from faker import Faker
from module.picking.saleorder.models import SaleOrder, PayTerm, Collection

faker = Faker()

class SaleOrderItemFactory:

    def build