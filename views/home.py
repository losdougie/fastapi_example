import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("templates") # jinja2 needs to be installed; e.g. serve files include aiofiles

router = fastapi.APIRouter() # like flask "blueprint" - breaks up to files/apps

@router.get("/", include_in_schema=False) # include in schema: False removes from docs page
def index(request: Request): #type hints work with fastapi to know how to use it
    return templates.TemplateResponse("index.html", {"request": request}) # request needed by Jinja
