from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://usr:pass@localhost:5001/work_org')

Base = declarative_base()
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

