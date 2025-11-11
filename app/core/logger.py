# Logs centralizados solo en archivo
import logging
from app.core.config import settings
 
logging.basicConfig(
   filename="app.log",
   level=settings.log_level,
   format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(settings.app_name)
#Logs irán a app.log en la raíz del proyecto.