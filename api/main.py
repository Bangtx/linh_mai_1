from fastapi import *
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

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
    return {"filename": file.filename}