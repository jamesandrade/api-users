from datetime import datetime
from peewee import PostgresqlDatabase, Model, CharField, DateTimeField , IntegerField
db = PostgresqlDatabase('mydatabase', host='localhost', port=5432, user='postgres', password='docker')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name=CharField()
    email=CharField(unique=True)
    password=CharField()
    avatar=CharField(null=True)
    created_at=DateTimeField(default=datetime.now)
    updated_at=DateTimeField(null=True)

#chave estrangeira: ForignKeyField(outra tabela, backref='users', null=True, default=None)
db.connect()
db.create_tables([User])
db.close()