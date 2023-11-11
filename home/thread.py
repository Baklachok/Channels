import random
import threading

from .models import *
from faker import Faker
fake = Faker()


class CreateStudentsThread(threading.Thread):
    def __init__(self , total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Thread execution started')
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total += 1
                student_obj = Students.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10 , 50)
                )
        except Exception as e:
            print(e)