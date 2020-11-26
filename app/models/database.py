import databases
import sqlalchemy
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

DB_DRIVER = config["data_base"]["driver"]
DB_USER = config["data_base"]["username"]
DB_PASSWORD = config["data_base"]["password"]
DB_HOST = config["data_base"]["host"]
DB_PORT = config["data_base"]["port"]
DB_NAME = config["data_base"]["name"]

DATABASE_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData(engine)

request_table = sqlalchemy.Table(
    "request_table",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("region", sqlalchemy.String)
)

counter_table = sqlalchemy.Table(
    "counter_table",
    metadata,
    sqlalchemy.Column("requestid", sqlalchemy.Integer, sqlalchemy.ForeignKey("request_table.id")),
    sqlalchemy.Column("counter", sqlalchemy.Integer),
    sqlalchemy.Column("timestamp", sqlalchemy.Integer)
)

metadata.create_all(engine, checkfirst=True)

