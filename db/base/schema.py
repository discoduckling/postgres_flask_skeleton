from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from engine import Base, engine


class Department(Base):
    __tablename__ = "departments"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)


departments = Department.__table__


class Employee(Base):
    __tablename__ = "employees"
    id = Column("id", Integer(), primary_key=True)
    name = Column("name", String(), nullable=False)
    created_on = Column("create_on", DateTime(), default=datetime.now)
    department_id = Column("department_id", Integer(), ForeignKey("departments.id"))

    department = relationship("Department", backref=backref("employees", uselist=True))


employees = Employee.__table__

Base.metadata.create_all(engine)
