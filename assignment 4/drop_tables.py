from peewee import SqliteDatabase
from models.Chequing import Chequing
from models.Savings import Savings

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()

db.drop_tables([Chequing, Savings])
