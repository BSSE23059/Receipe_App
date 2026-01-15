from faker import Faker
from .models import *
fake = Faker()
import random

def seed_db(n=10) -> None:
    try:
        for _ in range(n):

            department_objects = Department.objects.all()
            department_index = random.randint(0, len(department_objects)-1)
            dept = Department.objects.create(
                department = department_objects[department_index].department
            )

            student_id = StudentID.objects.create(
                student_id = f"BSCS230{random.randint(2,19)}"
            )

            StudentProfile.objects.create(
                department = dept,
                student_id = student_id,
                student_name = fake.name(),
                student_email = fake.unique.email(),
                student_age = fake.random_int(min=18, max=30),
                student_address = fake.address()
            )
    except Exception as e:
        print(f"An error occurred: {e}")