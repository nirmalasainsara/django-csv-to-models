from django.urls import path
from . import apiviews

app_name = "empsheet"

urlpatterns = [
    path(
        "employees/",
        apiviews.employee_list_view.as_view(),
        name="employee_list_view",
    ),
]