# create_tables.py

from app.database import engine
from app.models import Base

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
