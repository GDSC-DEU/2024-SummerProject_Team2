from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class AllProblem(Base):
    __tablename__ = 'allproblem'
    problem_name = Column(String(255), nullable=False)
    problem_number = Column(Integer, primary_key=True, nullable=False)
    problem_tier = Column(Integer, nullable=False)

class UnsolvedProblem(Base):
    __tablename__ = 'unsolved_problem'
    problem_name = Column(String(255), nullable=False)
    problem_number = Column(Integer, primary_key=True, nullable=False)
    problem_tier = Column(Integer, nullable=False)

