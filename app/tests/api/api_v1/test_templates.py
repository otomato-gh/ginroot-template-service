from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.template import create_random_template


def test_create_template(
    client: TestClient, db: Session
) -> None:
    data = {
        "language": "python",
        "framework": "fastapi",
        "app_type": "backend",
        "db_type": "postgres",
        "cloud_provider": "aws",
        "iac_type": "cdk",
        "deployment_type": "ecs",
        "repo_url": "test_url"
    }

    response = client.post(
        f"{settings.API_V1_STR}/templates/",  json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["language"] == data["language"]
    assert content["framework"] == data["framework"]
    assert content["app_type"] == data["app_type"]
    assert content["db_type"] == data["db_type"]
    assert content["cloud_provider"] == data["cloud_provider"]
    assert content["iac_type"] == data["iac_type"]
    assert content["deployment_type"] == data["deployment_type"]
    assert content["repo_url"] == data["repo_url"]
    assert "id" in content


def test_read_template_by_id(
    client: TestClient, db: Session
) -> None:
    template = create_random_template(db)
    response = client.get(
        f"{settings.API_V1_STR}/templates/{template.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["language"] == template.language
    assert content["framework"] == template.framework
    assert content["app_type"] == template.app_type
    assert content["db_type"] == template.db_type
    assert content["cloud_provider"] == template.cloud_provider
    assert content["iac_type"] == template.iac_type
    assert content["deployment_type"] == template.deployment_type
    assert content["repo_url"] == template.repo_url
    assert content["id"] == template.id


def test_read_template_by_parameters(
        client: TestClient, db: Session
) -> None:
    template = create_random_template(db)
    data = {
        "language": template.language,
        "framework": template.framework,
        "app_type": template.app_type,
        "db_type": template.db_type,
        "cloud_provider": template.cloud_provider,
        "iac_type": template.iac_type,
        "deployment_type": template.deployment_type,
        "repo_url": template.repo_url
    }
    response = client.get(
        f"{settings.API_V1_STR}/templates/",
        json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["language"] == template.language
    assert content["framework"] == template.framework
    assert content["app_type"] == template.app_type
    assert content["db_type"] == template.db_type
    assert content["cloud_provider"] == template.cloud_provider
    assert content["iac_type"] == template.iac_type
    assert content["deployment_type"] == template.deployment_type
    assert content["repo_url"] == template.repo_url
    assert content["id"] == template.id


def test_read_all_templates(
    client: TestClient, db: Session
) -> None:
    template = create_random_template(db)
    response = client.get(
        f"{settings.API_V1_STR}/templates/all"
    )
    assert response.status_code == 200
    content = response.json()
    print(content)
    assert len(content) > 0
