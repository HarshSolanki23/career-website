import os
from sqlalchemy import create_engine, text

db_connecttion_string =  os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connecttion_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


    
