from app.models import Hospital
from app.schemas import HospitalCreate, HospitalResponse
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models import Hospital
from app.schemas import HospitalCreate, HospitalResponse, HospitalUpdate

router = APIRouter()

@router.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that provides basic information about the Hospital Directory API
    """
    return {
        "message": "Welcome to the Hospital Directory API",
        "version": "1.0.0",
        "description": "API for managing hospital information",
        "endpoints": {
            "hospitals": "/hospitals",
            "get_hospital": "/hospitals/{hospital_id}",
            "create_hospital": "POST /hospitals",
            "update_hospital": "PUT /hospitals/{hospital_id}",
            "delete_hospital": "DELETE /hospitals/{hospital_id}"
        },
        "docs": "/docs",
        "redoc": "/redoc"
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/hospitals", response_model=HospitalResponse, status_code=201)
def create_hospital(hospital: HospitalCreate, db: Session = Depends(get_db)):
    db_hospital = Hospital(**hospital.dict())
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital

@router.get("/hospitals", response_model=List[HospitalResponse])
def read_hospitals(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, le=50),
    db: Session = Depends(get_db)
):
    hospitals = db.query(Hospital).offset(skip).limit(limit).all()
    return hospitals

@router.get("/hospitals/{hospital_id}", response_model=HospitalResponse)
def get_hospital(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@router.put("/hospitals/{hospital_id}", response_model=HospitalResponse)
def update_hospital(hospital_id: int, updates: HospitalUpdate, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(hospital, field, value)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.delete("/hospitals/{hospital_id}")
def delete_hospital(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital not found")
    db.delete(hospital)
    db.commit()
    return {"message": "Hospital deleted"}
