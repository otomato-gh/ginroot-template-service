INSERT INTO template (language, framework, app_type, db_type, cloud_provider, iac_type, deployment_type, repo_url)
VALUES ('python', 'fastapi', 'backend', 'postgres', 'aws', 'cdk', 'ecs', 'otomato-gh/pull-test-ginroot');

INSERT INTO template (language, framework, app_type, db_type, cloud_provider, iac_type, deployment_type, repo_url)
VALUES ('python', 'flask', 'backend', 'mysql', 'azure', 'terraform', 'vm', 'otomato-gh/pull-test-ginroot');

INSERT INTO template (language, framework, app_type, db_type, cloud_provider, iac_type, deployment_type, repo_url)
VALUES ('go', 'gin', 'backend', 'mongodb', 'aws', 'terraform', 'kubernetes', 'otomato-gh/pull-test-ginroot');
