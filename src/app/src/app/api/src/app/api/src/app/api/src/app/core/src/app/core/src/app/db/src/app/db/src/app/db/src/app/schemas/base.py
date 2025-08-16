from pydantic import BaseModel

class CompetitorIn(BaseModel):
    name: str
    domain: str

class CompetitorOut(CompetitorIn):
    id: int
