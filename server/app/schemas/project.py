from pydantic import BaseModel
import uuid
from typing import Optional

class ProjectCreate(BaseModel):
    title: str
    description: str
    github_link: str
    live_link: str
    featured: bool = False

class ProjectUpdate(BaseModel):
    title : Optional[str] = None
    description : Optional[str]= None
    github_link : Optional[str] = None
    live_link : Optional[str]= None
    featured : Optional[bool] = None

class ProjectResponse(BaseModel):
    id: uuid.UUID
    title : str
    description : str
    github_link : str
    live_link : str
    featured : bool

    class Config:
        from_attributes = True