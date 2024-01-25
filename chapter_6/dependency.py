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
