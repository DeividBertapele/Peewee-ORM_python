from datetime import datetime
from peewee import (
    SqliteDatabase, Model, TextField, ForeignKeyField, DateTimeField, IntegerField )


db = SqliteDatabase("notas.db") # cria database


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel): # Criar a tbela Pessoa
    nome= TextField()
    email= TextField(unique=True)
    senha= TextField()
    idade = IntegerField()


class Grupo(BaseModel): # Cria a tabela Grupo
    nome =  TextField()
    dona = ForeignKeyField(Pessoa, backref="grupos")
    
    
class Nota(BaseModel): # Cria a tabela Nota
    dona = ForeignKeyField(Pessoa, backref='notas')
    grupo = ForeignKeyField(Grupo, backref='notas', null=True, default=None)
    titulo = TextField()
    nota = TextField()
    criado_em = DateTimeField(default=datetime.now)
    modificado_em = DateTimeField()  
    

    
        
Pessoa.create_table() # Criar a tabela

db.create_tables([Grupo, Nota]) # Cria a tabela no banco de dados