# -*- coding: utf-8 -*-
"""
    db
    ~~

    :copyright: (c) 2017-18 by Wendell Hu.
    :license: MIT, see LICENSE for more details.
"""

import os

from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import SPIDER_DATABASE_URI

Base = declarative_base()
engine = create_engine(SPIDER_DATABASE_URI)
session_generator = sessionmaker(bind=engine)


class Article(Base):
    """Similar to the ORM mapping in server.models package, but these articles
    are just for the algorithm module. Maybe the database may be switched to
    another one.
    """
    __tablename__ = 'articles'

    _id = Column(Integer(), primary_key=True)
    title = Column(String(256), index=True)
    uri = Column(String(256))
    content = Column(Text())
    source = Column(String(128))
    crawled_at = Column(String(128), nullable=True)
    published_at = Column(String(128), nullable=True)
    editor = Column(String(128), nullable=True)
    published_time = Column(String(128), nullable=True)


Base.metadata.create_all(bind=engine)
