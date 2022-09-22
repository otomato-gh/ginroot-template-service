from typing import Optional

from pydantic import BaseModel


# Shared properties
class TemplateBase(BaseModel):
    language: str
    framework: Optional[str] = None
    app_type: Optional[str] = None
    db_type: Optional[str] = None
    cloud_provider: str
    iac_type: str
    deployment_type: str
    repo_url: Optional[str] = None


# Properties to receive on item creation
class TemplateCreate(TemplateBase):
    pass


# Properties to receive on item update
class TemplateGet(TemplateBase):
    pass


# Properties shared by models stored in DB
class TemplateInDBBase(TemplateBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Template(TemplateInDBBase):
    pass


# Properties stored in DB
class TemplateInDB(TemplateInDBBase):
    pass
