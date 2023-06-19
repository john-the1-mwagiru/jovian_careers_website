import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://cy463hr4ilq857b97arl:pscale_pw_KmdPmv5R1dGbq6MIJoB3UGLwexhiPQiSAS2ByWSIrLD@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  column_names=result.keys()
  jobs=[]
  for row in result.all():
    jobs.append(dict(zip(column_names,row)))
  return jobs