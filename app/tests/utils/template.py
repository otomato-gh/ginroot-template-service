from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.template import TemplateCreate
from app.tests.utils.utils import random_lower_string


def create_random_template(db: Session) -> models.Template:
    language = random_lower_string()
    framework = random_lower_string()
    app_type = random_lower_string()
    db_type = random_lower_string()
    cloud_provider = random_lower_string()
    iac_type = random_lower_string()
    deployment_type = random_lower_string()
    repo_url = random_lower_string()
    template_in = TemplateCreate(language=language, framework=framework, app_type=app_type, db_type=db_type,
                                 cloud_provider=cloud_provider, iac_type=iac_type, deployment_type=deployment_type,
                                 repo_url=repo_url, id=id)
    return crud.template.create_template(db=db, template_in=template_in)
