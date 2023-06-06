from .queries import (
    query_get_request_quantity_by_saleorder,
    query_get_picking_quantity_by_saleorder,
    query_get_picking_quantity_by_customer, 
    query_get_request_quantity_by_customer
)
from wmsbk.settings.local import DATABASES

import psycopg2

class ConnSQLite3:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'],
                host=DATABASES['default']['HOST'],
                port=DATABASES['default']['PORT'],
                database=DATABASES['default']['NAME']
            )
            self.cursor = self.connection.cursor()
            #print("successful connection!")
        except Exception as e:
            print(e)
        
    def get_picking_quantity_by_customer(self, name_customer, schema_name):
        """
         Suma todas las referencias que tengo despachadas de un cliente
        """
        sql = query_get_picking_quantity_by_customer(name_customer, schema_name)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            picking_quantity = {
                'quantity': data[0]
            }
            #print("Consulta realizada con exito!")
            #print(f"Resultado: {picking_quantity}\n")
            self.close()
            return picking_quantity
        except Exception as e:
            print(f"Ocurrio un error al consultar la base de datos.\nError: {e}\n")
            raise

    def get_request_quantity_by_customer(self, name_customer, schema_name):
        """
        Suma todas las referencias que tengo solicitadas por un cliente
        """
        sql = query_get_request_quantity_by_customer(name_customer, schema_name)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            request_quantity = {
                'quantity': data[0]
            }
            #print("Consulta realizada con exito!")
            #print(f"Resultado: {request_quantity}\n")
            self.close()
            return request_quantity
        except Exception as e:
            print(f"Ocurrio un error al consultar la base de datos.\nError: {e}\n")
            raise

    def get_picking_quantity_by_saleorder(self, sale_order, schema_name):
        """
        Suma todas las referencias que tengo despachadas de una orden de venta
        """
        sql = query_get_picking_quantity_by_saleorder(sale_order, schema_name)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            picking_quantity = {
                'quantity': data[0]
            }
            #print("Consulta realizada con exito!")
            #print(f"Resultado: {picking_quantity}\n")
            self.close()
            return picking_quantity
        except Exception as e:
            print(f"Ocurrio un error al consultar la base de datos.\nError: {e}\n")
            raise

    def get_request_quantity_by_saleorder(self, sale_order, schema_name):
        """
        Suma todas las referencias que tengo solicitadas de una orden de venta
        """
        sql = query_get_request_quantity_by_saleorder(sale_order, schema_name)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            request_quantity = {
                'quantity': data[0]
            }
            #print("Consulta realizada con exito!")
            #print(f"Resultado: {request_quantity}\n")
            self.close()
            return request_quantity
        except Exception as e:
            print(f"Ocurrio un error al consultar la base de datos.\nError: {e}\n")
            raise
    
    def close(self):
        self.connection.close()