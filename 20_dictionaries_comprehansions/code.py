users = [
    (0, "Bob", "paasss"),
    (1, "Max", "1111"),
    (2, "Ann", "123"),
    (3, "Tim", "wirh2")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password == password_input:
    print("You are logged")
else:
    print("Wrong credentials")

