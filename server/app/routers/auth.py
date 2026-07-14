from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.admin import Admin
from app.schemas.authentication import AdminCreate, AdminResponse,AdminLogin,Token
from app.utilis.security import hash_password, verify_password,create_access_token

router = APIRouter(prefix="/admin", tags=["Authentication"])

@router.post("/register", response_model=AdminResponse, status_code=status.HTTP_201_CREATED)
def register_admin(
    admin: AdminCreate,
    db: Session = Depends(get_db)
):
    existing_admin = db.query(Admin).filter(Admin.email == admin.email).first()
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin with this email already exists."

        )
    hashed_password = hash_password(admin.password)
    new_admin = Admin(
        email=admin.email,
        password_hashed=hashed_password
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


@router.post("/login", response_model=Token)
def login_admin(
    admin: AdminLogin,
    db: Session = Depends(get_db)
):
    existing_admin = db.query(Admin).filter(Admin.email == admin.email).first()
    if not existing_admin or not verify_password(admin.password, existing_admin.password_hashed):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    access_token = create_access_token(data={"sub": str(existing_admin.id)})
    return {"access_token": access_token, "token_type": "bearer"}