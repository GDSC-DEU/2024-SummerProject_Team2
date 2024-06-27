from typing import List, Optional
from pydantic import BaseModel

class AllProblem(BaseModel):
    problem_name: str
    problem_number: int
    problem_tier: int

    class Config:
        orm_mode = True


class UnsovledProblem(BaseModel):
    problem_name: str
    problem_number: int
    problem_tier: int

    class Config:
        orm_mode = True
