def query_get_picking_quantity_by_customer(name_customer, schema):
    """Suma todas las referencias que tengo despachadas de un cliente"""
    sql = f"""
        SELECT 
            CASE 
				WHEN SUM(T3.quantity) is null 
				THEN 0
				ELSE SUM(T3.quantity)
			END
        FROM
            {schema}.saleorder_saleorder T0
            INNER JOIN {schema}.picking_picking T1 ON T0.id = T1.sale_order_id
            INNER JOIN {schema}.box_box T2 ON T1.id = T2.picking_id
            INNER JOIN {schema}.boxitem_boxitem T3 ON T2.id = T3.box_id
        WHERE
            T0.customer_name = '{name_customer}'
    """
    return sql

def query_get_request_quantity_by_customer(name_customer, schema):
    """Suma todas las referencias que tengo solicitadas por un cliente"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T1.quantity) is null 
				THEN 0
				ELSE SUM(T1.quantity)
			END
        FROM
            {schema}.saleorder_saleorder T0
            INNER JOIN {schema}.saleorderitem_saleorderitem T1 ON T0.id = T1.sale_order_id
        WHERE
            T0.customer_name = '{name_customer}'
    """
    return sql

def query_get_picking_quantity_by_saleorder(sale_order, schema):
    """Suma todas las referencias que tengo despachadas de una orden de venta"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T3.quantity) is null 
				THEN 0
				ELSE SUM(T3.quantity)
			END
        FROM
            {schema}.saleorder_saleorder T0
            INNER JOIN {schema}.picking_picking T1 ON T0.id = T1.sale_order_id
            INNER JOIN {schema}.box_box T2 ON T1.id = T2.picking_id
            INNER JOIN {schema}.boxitem_boxitem T3 ON T2.id = T3.box_id
        WHERE
            T0.no_sale_order = '{sale_order}'
    """
    return sql

def query_get_request_quantity_by_saleorder(sale_order, schema):
    """Suma todas las referencias que tengo solicitadas de una orden de venta"""
    sql = f"""
        SELECT
            CASE 
				WHEN SUM(T1.quantity) is null 
				THEN 0
				ELSE SUM(T1.quantity)
			END
        FROM
            {schema}.saleorder_saleorder T0
            INNER JOIN {schema}.saleorderitem_saleorderitem T1 ON T0.id = T1.sale_order_id
        WHERE
            T0.no_sale_order = '{sale_order}'
    """
    return sql