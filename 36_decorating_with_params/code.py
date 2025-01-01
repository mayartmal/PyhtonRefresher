import functools

user = {"username": "jose", "level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "No admin permission"
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "Master_Password"




print(get_password("billing"))
