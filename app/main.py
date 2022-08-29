from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Inputs(BaseModel):
    language: str
    framework: Optional[str] = None
    app_type: Optional[str] = None
    db_type: Optional[str] = None
    cloud_provider: str
    iac_type: str
    deployment_type: str


app = FastAPI()


@app.post("/inputs/")
async def create_item(inputs: Inputs):
    # temporary returning inputs
    return inputs
