from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:nishkaks@localhost:5434/employee_db"
)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print("Connection failed:", e)