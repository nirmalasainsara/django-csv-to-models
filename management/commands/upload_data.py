import os
import csv
from django.core.management.base import BaseCommand
from empsheet.models import Employee
from django.conf import settings


class Command(BaseCommand):
    help = "upload csv to django model"

    def handle(self, *args, **kwargs):
        path = os.path.join(settings.BASE_DIR, "emp.csv")
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
                    Employee.objects.create(
                        employee_id=row[0],
                        firstname=row[1],
                        lastname=row[2],
                        city=row[3],
                    )
        print("data uploaded")