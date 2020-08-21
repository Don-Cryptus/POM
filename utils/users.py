from operator import itemgetter

# we can store test data in this module like users
users = [{"name": "valid_user", "email": "don.cryptus1@gmail.com", "password": "cryptus123", "provider": "google", "age": "18", "gender": "male"}]


def get_user(name):
    name = name
    return {"name": "valid_user", "email": "don.cryptus1@gmail.com", "password": "cryptus123", "provider": "google", "age": "18", "gender": "male"}
print(get_user("google"))
