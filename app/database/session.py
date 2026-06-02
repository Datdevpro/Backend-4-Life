from app.database.connection import SessionLocal

# Mỗi request sẽ cần một database session.

# Request đến
# → mở DB session
# → xử lý
# → đóng DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()