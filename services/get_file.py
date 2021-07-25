from models.data import FileRequest
from pathlib import Path

async def get_named_file(file_req: FileRequest):
    file_path = Path(str(__file__))
    file_parent = file_path.parent.absolute()
    folder_parent = file_parent.parent
    files_dir = folder_parent.joinpath("files")
    if not files_dir.is_dir():
        return None
    file_path = files_dir.joinpath(file_req.filename)
    if not file_path.is_file():
        return None
    return str(file_path)
