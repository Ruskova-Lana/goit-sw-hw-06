from database import SessionLocal
from models import Grade

session = SessionLocal()

grade = session.query(Grade).first()
print(grade)

session.close()