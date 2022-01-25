from fastapi import *
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

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
    # file_location = f"file/{file.filename}"
    # with open(file_location, "wb+") as file_object:
    #     file_object.write(file.file.read())
    imgs = os.listdir('file/yes')
    print(imgs)
    return {"name": file.filename, 'yes': file.filename in imgs}


@api.get("/vector_image")
def image_endpoint(name: str):
    return FileResponse(f'file/result/{name}')


@api.get("/vector")
def image_endpoint(name: str):
    return FileResponse(f'file/test/{name}')