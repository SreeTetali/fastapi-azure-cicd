from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API")

# --- CORS Configuration ---
# This is required so your separate frontend server can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace "*" with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/visitors/")
def create_visitor(name: str, message: str, db: Session = Depends(get_db)):
    new_visitor = models.Visitor(name=name, message=message)
    db.add(new_visitor)
    db.commit()
    return {"status": "success", "name": name}

@app.get("/api/visitors/")
def read_visitors(db: Session = Depends(get_db)):
    return db.query(models.Visitor).all()