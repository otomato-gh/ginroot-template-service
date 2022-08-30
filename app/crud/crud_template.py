from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.template import Template
from app.schemas.template import TemplateGet, TemplateCreate


class CRUDTemplate(CRUDBase[Template, TemplateGet, TemplateCreate]):
    def create_template(self, db: Session, *, obj_in: TemplateCreate) -> Template:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_template_by_parameters(self, db: Session, *, language: str, framework: str, app_type: str, db_type: str,
                                   cloud_provider: str, iac_type: str, deployment_type: str) -> List[Template]:
        return (
            db.query(self.model)
            .filter(Template.language == language, Template.framework == framework, Template.app_type == app_type,
                    Template.db_type == db_type, Template.cloud_provider == cloud_provider, Template.iac_type == iac_type,
                    Template.deployment_type == iac_type).all()
        )


item = CRUDTemplate(Template)
