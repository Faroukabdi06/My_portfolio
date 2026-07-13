from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.base import Base

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )
    password_hashed: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )