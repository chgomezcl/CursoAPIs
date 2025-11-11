# Aplicación FastAPI principal
from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.core.logger import logger
from app.routers.user_router import router as user_router
 
# Spanish comment: crear tablas al iniciar
Base.metadata.create_all(bind=engine)
 
app = FastAPI(title=settings.app_name)
 
# Spanish comment: incluir routers
app.include_router(user_router)
 
@app.on_event("startup")
async def startup_event():
   logger.info("App started successfully")

app = FastAPI(title=settings.app_name)
 
# Spanish comment: incluir routers
app.include_router(user_router)
 
@app.on_event("startup")
async def startup_event():
   logger.info("App started successfully")
 
@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
 
# uvicorn app.main:app --reload solucion detail not fount