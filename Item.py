from peewee import *

db = SqliteDatabase('items.db')

class BaseModel(Model):
    class Meta:
        database = db  # This model uses items.db database, comment like peewee docs

class Owner(BaseModel):
    name = CharField()

class Item(BaseModel):
    owner = ForeignKeyField(Owner, related_name='items')
    name = CharField()
    date = DateField()

'''
create tables, but check if they exist first
'''
def createTables():
    db.connect()
    db.create_tables([Owner, Item], True)

'''
delete tables
'''
def deleteTables():
    db.connect()
    db.drop_tables([Owner, Item])