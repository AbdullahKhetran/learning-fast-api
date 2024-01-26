# Dependecy:
#   specific information required at some time
# Dependency Injection:
#   pass any specific information into the function that it requires


from fastapi import FastAPI, Depends, Params

app = FastAPI()


# dependency function
def user_dep(name: str = Params, password: str = Params):
    return {"name": name, "valid": True}


# path function / web endpoint
@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


# Path decorater in preceding line
# in case dependency funtion just checks something and doesn't return any values

def check_dep(name: str = Params, password: str = Params):
    if not name:
        raise


# path decorater
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True
