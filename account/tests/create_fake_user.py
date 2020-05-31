import inject
from faker import Faker


@inject.autoparams()
def create_fake_user(faker: Faker):
    return {
        'first_name': faker.last_name(),
        'last_name': faker.last_name(),
        'email': faker.email(),
        'phone_number': faker.phone_number(),
        'address': faker.address(),
    }
