from sqlalchemy.orm import Session

from schemas.jobs import JobCreate

from db.models.job import Job


def create_new_job(job: JobCreate, db: Session, owner_id:int): 
    job = Job(**job.dict(), owner_id = owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job 


def retreive_job(id: int, db:Session):
    job = db.query(Job).filter(Job.id==id).first()
    return job 