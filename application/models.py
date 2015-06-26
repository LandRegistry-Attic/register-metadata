from sqlalchemy import Column, String
from application import db


class cre(db.Model):

    __tablename__ = 'cre'

    code = Column(String, primary_key=True)
    template = Column(String)
    infills = Column(String)
