from tests.test_setup import TestSetup
from tests.factories.expense_manager.expense_factories import SaleOrderFactory

class ExpenseTestCase(TestSetup):
    def test_search_sale_order(self):
        saleorder = SaleOrderFactory().create_sale_order()
        reponse = self.client.get(
            '/expense/expense/search'
        )