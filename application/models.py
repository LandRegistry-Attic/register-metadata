from sqlalchemy import Column, String, Integer
from application import db


class cre(db.Model):

    __tablename__ = 'cre'

    code = Column(String, primary_key=True)
    version = Column(Integer, primary_key=True)
    template = Column(String)
    infills = Column(String)


class mdref(db.Model):

    __tablename__ = 'mdref'

    code = Column(String)
    version = Column(Integer)
    mdref = Column(String, primary_key=True)
    sequence = Column(Integer, primary_key=True)
    entry_id = Column(Integer, primary_key=True)
