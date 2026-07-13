from sqlalchemy import String, Integer, Column, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database.base import Base

class Project(Base):
    __tablename__ = "projects"

    id :Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4
        )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False)
    github_link: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    live_link: Mapped[str] = mapped_column(
        String(255),
        nullable=False)

    featured: Mapped[bool] = mapped_column(
        nullable=False,
        default=False)