import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="mortal_kombat_db",
            user="admin",
            password="adminpassword",
            host="localhost",
            port=5432
        )
        return conn
    except Exception as e:
        print("Error de conexión a la base de datos:", e)
        return None