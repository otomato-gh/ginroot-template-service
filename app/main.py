from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Inputs(BaseModel):
    language: str
    framework: Union[str, None] = None
    app_type: Union[str, None] = None
    db_type: Union[str, None] = None
    cloud_provider: str
    iac_type: str
    deployment_type: str


app = FastAPI()


@app.post("/inputs/")
async def create_item(inputs: Inputs):
    # temporary returning inputs
    return inputs
