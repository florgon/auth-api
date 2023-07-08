"""
    Database core. 
    Contains engine and ORM related stuff.
"""

from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError, IntegrityError
from sqlalchemy import create_engine, MetaData
from app.config import get_logger, Settings

settings = Settings()
engine = create_engine(
    url=settings.database_dsn,
    pool_size=settings.database_pool_size,
    max_overflow=settings.database_max_overflow,
    pool_timeout=settings.database_pool_timeout,
    pool_recycle=settings.database_pool_recycle,
    poolclass=QueuePool,
    pool_pre_ping=True,
)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, expire_on_commit=True, bind=engine
)


def create_all() -> None:
    """
    Creating all database metadata.
    Currently there is only ORM metadata builder.
    !TODO: Migrations with alembic.
    """
    try:
        metadata.create_all(bind=engine)
    except (IntegrityError, OperationalError) as e:
        get_logger().error(
            f"[database_core] Failed to do `create_all` as metadata raised: `{e}`"
        )
