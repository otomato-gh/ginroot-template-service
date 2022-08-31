from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class Template(Base):
    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, nullable=False)
    framework = Column(String)
    app_type = Column(String)
    db_type = Column(String)
    cloud_provider = Column(String, nullable=False)
    iac_type = Column(String, nullable=False)
    deployment_type = Column(String, nullable=False)
    url = Column(String, nullable=False)
