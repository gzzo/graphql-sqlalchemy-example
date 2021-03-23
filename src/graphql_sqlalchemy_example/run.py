from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from graphql_sqlalchemy import build_schema
from fastapi import FastAPI
from ariadne.asgi import GraphQL

from .models import User, Book
from .base import Base

engine = create_engine('sqlite:///config.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    Base.metadata.create_all(engine)


def seed():
    if session.query(User).all():
        return

    u = User(name='alex', books=[Book(name='sapiens'), Book(name='einstein')])

    session.add(u)
    session.commit()


init_db()
seed()
app = FastAPI(debug=True)
schema = build_schema(Base)
app.mount("/graphql", GraphQL(schema, context_value=dict(session=session)))
