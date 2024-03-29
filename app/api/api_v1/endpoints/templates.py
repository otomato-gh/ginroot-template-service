from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/all", response_model=List[schemas.Template])
def get_all_templates(
        *,
        db: Session = Depends(deps.get_db) 
) -> Any:
    templates = crud.template.get_all_templates(db=db)
    return templates

@router.get("/", response_model=schemas.Template)
def get_template_by_parameters(
        *,
        db: Session = Depends(deps.get_db),
        template_get: schemas.TemplateGet
) -> Any:
    template = crud.template.get_template_by_parameters(db=db, template_get=template_get)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.get("/{id}", response_model=schemas.Template)
def get_template_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    template = crud.template.get_template_by_id(db=db, template_id=id)
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.post("/", response_model=schemas.Template)
def create_template(
    *,
    db: Session = Depends(deps.get_db),
    template_in: schemas.TemplateCreate
) -> Any:
    template = crud.template.create_template(db=db, template_in=template_in)
    return template
