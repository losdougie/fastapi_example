import fastapi
import uvicorn
from views import home
from api import data_api

api = fastapi.FastAPI()

def configure():
    # import routers from other files (imported above)
    api.include_router(home.router)
    api.include_router(data_api.router)

def main():
    uvicorn.run(api)

configure()
if __name__ == "__main__":
    main()


