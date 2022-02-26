from fastapi import *
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from sqlalchemy.orm import Session
from sql_app import models, schemas
from sql_app.database import SessionLocal, engine
from sql_app.schemas import Patient
import sql_app.models as models

api = FastAPI()
models.Base.metadata.create_all(bind=engine)
url = 'https://backendlinhmai.herokuapp.com//'
origins = ["*"]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@api.post('/add_patient')
def add_patient(patient: Patient, db: Session = Depends(get_db)):
    data = models.Patient(**patient.dict())
    patients = get_patient(db)
    names = list(map(lambda x: x.name, patients))
    if patient.name in names:
        return {'msg': 'patient already exists'}
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@api.get('/get_patients')
def get_patient(db: Session = Depends(get_db)):
    result = db.query(models.Patient).all()
    return result


@api.delete('/delete_patient/{id}')
def delete_patient(id: int, db: Session = Depends(get_db)):
    data = db.query(models.Patient).get(id)
    db.delete(data)
    db.commit()
    return {'msg': 'deleted'}


@api.post("/users/", response_model=schemas.User)
def create_user_api(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user