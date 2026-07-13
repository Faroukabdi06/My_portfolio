from fastapi import FastAPI
from app.routers.projects import router as projects_router
from app.routers.auth import router as auth_router

app = FastAPI()

app.include_router(projects_router)
app.include_router(auth_router)



@app.get("/")
def root():
    return {"message": "Portfolio API is running successfully!"}