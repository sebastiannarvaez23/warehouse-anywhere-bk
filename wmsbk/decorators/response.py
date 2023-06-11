from rest_framework import status
from datetime import datetime

def add_consumption_detail_decorator(view_func):
    def wrapper(*args, **kwargs):
        response = view_func(*args, **kwargs)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.data = {
            "status": status.HTTP_200_OK,
            "message": "OK",
            "resolved_at": current_datetime,
            "next_url": response.next_url,
            "data": response.data,
        }
        return response
    return wrapper
