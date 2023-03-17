from rest_framework import status
from tests.test_setup import TestSetup
from tests.picking.factories.saleorder.saleorder_factories import SaleOrderFactory

class SaleOrderTestCase(TestSetup):

    url = '/saleorder/'

    def test_list(self):
        saleorder = SaleOrderFactory().create_sale_order()
        response = self.client.get(
            self.url + saleorder.no_sale_order + '/',
            format = 'json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['no_sale_order'], saleorder.no_sale_order)
        self.assertEqual(response.data['publication_date'], saleorder.publication_date.strftime('%Y-%m-%d'))
        self.assertEqual(response.data['delivery_date'], saleorder.delivery_date.strftime('%Y-%m-%d'))
        self.assertEqual(response.data['doc_date'], saleorder.doc_date.strftime('%Y-%m-%d'))
        self.assertEqual(response.data['po_comments'], saleorder.po_comments)
        self.assertEqual(response.data['customer_name'], saleorder.customer_name)
        self.assertEqual(response.data['delivery_address'], saleorder.delivery_address)
        self.assertEqual(response.data['pay_term'], saleorder.pay_term.name)
        self.assertEqual(response.data['collection'], saleorder.collection.name)
