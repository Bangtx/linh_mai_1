from fastapi import *
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()
url = 'http://127.0.0.1:8000/'
origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.post('/image')
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"file/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"name": file.filename}


@api.get("/vector_image")
def image_endpoint(name: str):
    return FileResponse(f'file/{name}')