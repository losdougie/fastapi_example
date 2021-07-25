from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/upload")

@router.get("/")
async def upload():
    content = """
<body>
<form action="/files/filesize/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/files/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)