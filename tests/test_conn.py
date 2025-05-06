from database import get_connection_gasolinera

try:
    with get_connection_gasolinera() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print("Conexión exitosa a la base de datos gasolinera:", db_name["DATABASE()"])
except Exception as e:
    print("Error al conectar a gasolinera:", e)