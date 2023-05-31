from sqlalchemy import create_engine, MetaData

# URL de conexión a la base de datos PostgreSQL en Supabase
db_url = "postgresql://postgres:nmaC9kFba7@vm6W@db.raredzkxqyzlbgijrlmh.supabase.co:5432/postgres"

# Crear el motor de SQLAlchemy para la conexión a la base de datos
engine = create_engine(db_url)

# Crear un objeto MetaData para trabajar con la base de datos
metadata = MetaData(bind=engine)