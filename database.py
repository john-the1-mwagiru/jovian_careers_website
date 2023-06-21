import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://r6ej1u0ai2pcjhrlcjxr:pscale_pw_Et0Q7juZIN2pjYb2FCr4zzcgsPPsUU5YVeWLR12BLjk@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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