import functools

user = {"username": "jose", "level": "guest"}




def make_secure(level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["level"] == level:
                return func(*args, **kwargs)
            else:
                return "No admin permission"
        return secure_function
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: usrpas"



print(get_admin_password())
print(get_dashboard_password())

user = {"username": "jose", "level": "admin"}


print(get_admin_password())
print(get_dashboard_password())