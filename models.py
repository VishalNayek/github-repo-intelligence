from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Repo(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True)
    owner = Column(String, nullable=False)
    name = Column(String, nullable=False)
    full_name = Column(String)
    description = Column(String)
    language = Column(String)
    topics = Column(String)
    stars = Column(Integer)
    forks = Column(Integer)
    open_issues = Column(Integer)
    default_branch = Column(String)