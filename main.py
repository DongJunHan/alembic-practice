import sqlalchemy
from fastapi import FastAPI, Depends, status, HTTPException

from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from model import User, Organization

from pydantic import BaseModel

app = FastAPI()


class CreateUserRequestSchema(BaseModel):
    name: str | None
    email: str
    password: str

@app.post('/users', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequestSchema, db: Session = Depends(get_db)):
    print(data)
    try:
        user = User(**data.dict())
    # user = data.from_orm()
        db.add(user)
        db.commit()
        db.refresh(user)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")
    return user


@app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    query = select(User).where(User.id == user_id)
    user = db.execute(query).scalar()
    return user


@app.get('/organizations', status_code=status.HTTP_200_OK)
async def get_organizations(db: Session = Depends(get_db)):
    query = select(Organization)
    return db.execute(query).scalars().all()


@app.post('/organizations', status_code=status.HTTP_201_CREATED)
async def create_organization(data: dict, db: Session = Depends(get_db)):
    organization = Organization(**data)
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization
