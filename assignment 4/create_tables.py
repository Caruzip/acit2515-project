from peewee import SqliteDatabase
from models.Savings import Savings
from models.Chequing import Chequing

db = SqliteDatabase('bank.sqlite', pragmas={'foreign_keys': 1})
db.connect()

db.create_tables([Chequing, Savings])