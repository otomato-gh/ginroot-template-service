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

    def get_template_by_id(self, db: Session, *, template_id: int) -> Template:
        return (
            db.query(self.model)
            .filter(Template.id == template_id)
            .first()
        )

    def get_template_by_parameters(self, db: Session, *, template: TemplateGet) -> Template:
        return (
            db.query(self.model)
            .filter(Template.language == template.language,
                    Template.framework == template.framework,
                    Template.app_type == template.app_type,
                    Template.db_type == template.db_type,
                    Template.cloud_provider == template.cloud_provider,
                    Template.iac_type == template.iac_type,
                    Template.deployment_type == template.deployment_type)
            .first()
        )

    # def get_template_by_app_type(self, db: Session, *, app_type: str) -> List[Template]:
    #     return (
    #         db.query(self.model)
    #         .filter(Template.app_type == app_type)
    #         .all()
    #     )


template = CRUDTemplate(Template)
