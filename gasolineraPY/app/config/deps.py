from app.config.database import SessionLocal

# Dependency (FastAPI) para obtener sesión en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()