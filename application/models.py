from sqlalchemy import Column, String, Integer
from application import db


class cre(db.Model):

    __tablename__ = 'cre'

    code = Column(String, primary_key=True)
    version = Column(Integer, primary_key=True)
    template = Column(String)
    infills = Column(String)
    restriction_name = Column(String)


class mdref(db.Model):

    __tablename__ = 'mdref'

    code = Column(String)
    version = Column(Integer)
    mdref = Column(String, primary_key=True)
    sequence = Column(Integer, primary_key=True)
    entry_id = Column(Integer, primary_key=True)

class role(db.Model):

    __tablename__ = 'role'

    entry_role_code = Column(String, nullable=False, primary_key=True)
    entry_role_seq_no = Column(Integer, nullable=True)
    reg_child_code = Column(String, nullable=False)
    cat_code = Column(String, nullable=False)
    entry_role_desc = Column(String, nullable=False)
    entry_status_code = Column(String, nullable=True)

class subrole(db.Model):

    __tablename__ = 'subrole'

    sub_role_code = Column(String, nullable=False, primary_key=True)
    entry_role_code = Column(String, nullable=False)
    sub_role_desc = Column(String, nullable=False)
