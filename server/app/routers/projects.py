from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import uuid
from typing import List

from app.database.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["projects"])


def get_project_or_404(project_id: uuid.UUID, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):

    new_project = Project(**project.model_dump())

    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.get("/", response_model=List[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    return get_project_or_404(project_id, db)


@router.patch("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: uuid.UUID,
    project_update: ProjectUpdate,
    db: Session = Depends(get_db)
):

    project = get_project_or_404(project_id, db)

    update_data = project_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project


@router.delete("/{project_id}")
def delete_project(project_id: uuid.UUID, db: Session = Depends(get_db)):

    project = get_project_or_404(project_id, db)

    db.delete(project)
    db.commit()

    return {"detail": "Project deleted successfully"}