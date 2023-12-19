from pydantic import BaseModel 

class Billboard(BaseModel):
    rank: int
    song: str
    artist: str
    year: int 