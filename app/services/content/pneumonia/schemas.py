from pydantic import BaseModel


class SPneumonia(BaseModel):
    type: str
    pathogen: str
    morbidity: float
    mortality: float
    severity: str
    symptoms: str


class SPneumoniaWithId(SPneumonia):
    id: int = 0
