from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/lenovo")
engine2 = create_engine("mysql+pymysql://root@localhost:3306/prueba")
meta = MetaData()
conn = engine.connect()
conn2 = engine2.connect()