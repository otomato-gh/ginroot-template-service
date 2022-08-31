from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.template import Template
from app.schemas.template import TemplateGet, TemplateCreate


class CRUDTemplate(CRUDBase[Template, TemplateGet, TemplateCreate]):
    def create_template(self, db: Session, *, template_in: TemplateCreate) -> Template:
        obj_in_data = jsonable_encoder(template_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_template_by_id(self, db: Session, *, template_id: int) -> Template:
        return (
            db.query(self.model)
            .filter(Template.id == template_id)
            .first()
        )

    def get_template_by_parameters(self, db: Session, *, template_get: TemplateGet) -> Template:
        return (
            db.query(self.model)
            .filter(Template.language == template_get.language,
                    Template.framework == template_get.framework,
                    Template.app_type == template_get.app_type,
                    Template.db_type == template_get.db_type,
                    Template.cloud_provider == template_get.cloud_provider,
                    Template.iac_type == template_get.iac_type,
                    Template.deployment_type == template_get.deployment_type)
            .first()
        )

    # def get_template_by_app_type(self, db: Session, *, app_type: str) -> List[Template]:
    #     return (
    #         db.query(self.model)
    #         .filter(Template.app_type == app_type)
    #         .all()
    #     )


template = CRUDTemplate(Template)
