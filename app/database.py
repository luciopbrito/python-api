from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

engine = create_engine(
  get_settings().database_url,
  pool_pre_ping=True,
  pool_recycle=36000
)

SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
)

def get_session():
  """Session factory"""

  session = SessionLocal()
  try:
    yield session
  finally:
    session.close()