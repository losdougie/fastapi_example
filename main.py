import fastapi
import uvicorn
from views import home, dl
from api import data_api, files
from fastapi.staticfiles import StaticFiles

api = fastapi.FastAPI()

def configure():
    #set up static files
    api.mount("/static", StaticFiles(directory="static"), name="static") # requires aiofiles
    # import routers from other files (imported above)
    api.include_router(home.router)
    api.include_router(data_api.router)
    api.include_router(files.router)
    api.include_router(dl.router)

def main():
    uvicorn.run(api)

configure()
if __name__ == "__main__":
    main()


