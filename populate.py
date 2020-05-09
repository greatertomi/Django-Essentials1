import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_two.settings')

import django
django.setup()

import random
from app_two.models import User
from faker import Faker

fake = Faker()
def populater(N=5):
  for entry in range(N):
    firstName = fake.first_name()
    lastName = fake.last_name()
    email = fake.email()

    person = User.objects.get_or_create(firstName=firstName, lastName=lastName, email=email)[0]

if __name__ == '__main__':
    print("populating script!")
    populater(20)
    print("populating complete!")
