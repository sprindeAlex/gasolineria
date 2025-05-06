import os
from contextlib import contextmanager
import pymysql
from pymysql.cursors import DictCursor

# Conexión a la base de datos gasolinera
@contextmanager
def get_connection_gasolinera():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            db="gasolinera",
            autocommit=True,
            cursorclass=DictCursor,
        )
        yield connection
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()