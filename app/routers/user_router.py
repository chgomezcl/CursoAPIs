# Endpoints de usuarios y healthcheck
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import SessionLocal
from app.models.user_model import User
from app.core.logger import logger
 
router = APIRouter(prefix="/users", tags=["Users"])
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
 
@router.post("/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        # Spanish comment: email duplicado → 409
        logger.warning("Attempt to create duplicated email: %s", email)
        raise HTTPException(status_code=409, detail="Email already exists")
    u = User(name=name, email=email)
    db.add(u)
    db.commit()
    db.refresh(u)
    logger.info("User created: %s", email)
    return u
 
@router.get("/healthcheck")
def healthcheck(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    logger.info("Healthcheck OK")
    return {"status": "ok"}