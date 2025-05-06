import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+aiomysql://root:@localhost/gasolinera"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def connect_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(lambda x: None)  # Prueba de conexión
        print("✅ Conexión a la base de datos establecida")
    except Exception as e:
        print("❌ Error al conectar a la base de datos:", e)