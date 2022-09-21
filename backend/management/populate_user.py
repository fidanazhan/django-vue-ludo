from faker import Faker
from account.models import CustomizeUser

fake = Faker()

for i in range(2):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + " " + last_name
    email = first_name + last_name + "@gmail.com"
    user = CustomizeUser(
        email=email,
        username=username
    )
    test = 'izad1614'
    user.set_password(test)
    user.save()
    