CREATE TABLE template (
    id integer primary key generated always as identity,
    language character varying(20) NOT NULL,
    framework character varying(20),
    app_type character varying(20),
    db_type character varying(20),
    cloud_provider character varying(20) NOT NULL,
    iac_type character varying(20) NOT NULL,
    deployment_type character varying(20) NOT NULL,
    repo_url character varying(255) NOT NULL
);
