from pydantic_settings import BaseSettings  # Spanish comment: configuración centralizada
 
class Settings(BaseSettings):
   database_url: str = "sqlite:///./test.db"
   app_name: str = "FastAPI_Production"
   log_level: str = "INFO"
 
   class Config:
       env_file = ".env"
 
settings = Settings()
 