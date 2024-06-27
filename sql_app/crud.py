from sqlalchemy.orm import Session

from . import models, schemas

def show_allproblems(db: Session, skip: int = 0):
    return db.query(models.AllProblem).offset(skip).all()

def show_unsolved_problem(db: Session, skip: int = 0):
    return db.query(models.UnsolvedProblem).offset(skip).all()