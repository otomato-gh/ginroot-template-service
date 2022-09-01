from sqlalchemy.orm import Session

from app import crud
from app.schemas.template import TemplateCreate, TemplateGet
from app.tests.utils.utils import random_lower_string


def test_create_template(db: Session) -> None:
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
    template = crud.template.create_template(db=db, template_in=template_in)
    assert template.language == language
    assert template.framework == framework
    assert template.app_type == app_type
    assert template.db_type == db_type
    assert template.cloud_provider == cloud_provider
    assert template.iac_type == iac_type
    assert template.deployment_type == deployment_type
    assert template.repo_url == repo_url


def test_get_template_by_id(db: Session) -> None:
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
    template = crud.template.create_template(db=db, template_in=template_in)
    stored_template = crud.template.get_template_by_id(db=db, template_id=template.id)
    assert stored_template
    assert template.id == stored_template.id
    assert template.language == stored_template.language
    assert template.framework == stored_template.framework
    assert template.app_type == stored_template.app_type
    assert template.db_type == stored_template.db_type
    assert template.cloud_provider == stored_template.cloud_provider
    assert template.iac_type == stored_template.iac_type
    assert template.deployment_type == stored_template.deployment_type
    assert template.repo_url == stored_template.repo_url


def test_get_template_by_parameters(db: Session) -> None:
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
    template = crud.template.create_template(db=db, template_in=template_in)
    template_get = TemplateGet(language=language, framework=framework, app_type=app_type, db_type=db_type,
                               cloud_provider=cloud_provider, iac_type=iac_type, deployment_type=deployment_type,
                               repo_url=repo_url, id=id)
    stored_template = crud.template.get_template_by_parameters(db=db, template_get=template_get)
    assert stored_template
    assert template.id == stored_template.id
    assert template.language == stored_template.language
    assert template.framework == stored_template.framework
    assert template.app_type == stored_template.app_type
    assert template.db_type == stored_template.db_type
    assert template.cloud_provider == stored_template.cloud_provider
    assert template.iac_type == stored_template.iac_type
    assert template.deployment_type == stored_template.deployment_type
    assert template.repo_url == stored_template.repo_url
