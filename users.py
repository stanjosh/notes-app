

user_list = {}


class User:
    def __init__(self, username, name, phone, state) -> None:
        self.username = username
        self.name = name
        self.phone = phone
        self.state = state
        self.profile = {'name': self.name,
                   'phone': self.phone,
                   'state': self.state}


def add_user(username, name, phone, state):
    new_user = User(username, name, phone, state)
    user_list[new_user.username] = new_user
    return new_user


def get_user(username):
    print(f'getting {username}')
    return user_list[username]
