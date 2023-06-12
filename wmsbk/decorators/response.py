from rest_framework import status
from datetime import datetime

def add_consumption_detail_decorator(view_func):
    def wrapper(*args, **kwargs):
        response = view_func(*args, **kwargs)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.data = {
                "status": response.status,
                "message": response.message,
                "resolved_at": current_datetime,
                "data": response.data
            }
        return response
    return wrapper

def add_saleorder_consumption_detail_decorator(view_func):
    def wrapper(*args, **kwargs):
        response = view_func(*args, **kwargs)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.data = {
                "status": response.status,
                "message": response.message,
                "resolved_at": current_datetime,
                "next_url": response.next_url,
                "before_url": response.before_url,
                "data": response.data
            }
        return response
    return wrapper