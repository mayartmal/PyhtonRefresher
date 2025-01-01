import functools

user = {"username": "jose", "level": "admin"}







def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["level"] == "admin":
            return func()
        else:
            return "No admin permission"
    return secure_function

@make_secure
def get_admin_password():
    return 1234


# def secure_get_admin_password():
#     if user["level"] == "admin":
#         return 1234

get_admin_password = make_secure(get_admin_password)

print(get_admin_password())
print(get_admin_password.__name__)
# print(secure_get_admin_password())