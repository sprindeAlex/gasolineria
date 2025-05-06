from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_connection_gasolinera

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def show_db_status(request: Request):
    try:
        with get_connection_gasolinera() as conn:
            with conn.cursor() as cursor:
                # Nombre de la base de datos
                cursor.execute("SELECT DATABASE();")
                db_name = cursor.fetchone()["DATABASE()"]

                # Obtener datos de la tabla clientes
                cursor.execute("SELECT id, nombre, tipo FROM clientes;")
                clientes = cursor.fetchall()

        return templates.TemplateResponse("index.html", {
            "request": request,
            "success": True,
            "db_name": db_name,
            "clientes": clientes
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "success": False,
            "error": str(e)
        })