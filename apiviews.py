from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Employee
from .serializer import (
    EmployeeSerializer,
)


class employee_list_view(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    """ 
    def get_queryset(self):
        query_set = Employee.objects.all()
        return query_set
    """