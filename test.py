import fastapi
import uvicorn

#Simplest example to test if fastapi is installed right.
api = fastapi.FastAPI()

@api.get("/")
def hello():
    return {
        "message": "Hello World"
    }

uvicorn.run(api)