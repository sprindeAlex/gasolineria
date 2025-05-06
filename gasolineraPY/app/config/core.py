import os
from datetime import datetime, timezone, timedelta

# Configuración de zona horaria
EUROPE_MADRID = timezone(timedelta(hours=2))  # CEST (+2 en verano)
# Usa pytz si lo necesitas más preciso

# URL base de la app
HOME_URL = "http://localhost:8000/"  # Cambiado al puerto 8000 de FastAPI

# Configuración de paginación
RECORDS_PER_PAGE = 200

def get_pagination_params(page: int):
    from_record_num = (RECORDS_PER_PAGE * page) - RECORDS_PER_PAGE
    return from_record_num