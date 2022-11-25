from ex_01 import Pessoa, Grupo, Nota


dados = Pessoa(
    nome="Python",
    idade="200",
    senha="12345",
    email="python@python.com",
    )


try:
    dados.save()
    Pessoa.create(
        nome="Peewee",
        idade="39",
        senha="12345898",
        email="peewee@maispython.com",
        )
except:
    ...
    
pessoas = [
    {'nome':'python1', 'email':'teste0@teste.com.br', 'idade':'1', 'senha':'12'},
    {'nome':'python2', 'email':'teste1@teste.com.br', 'idade':'1', 'senha':'123'},
    {'nome':'python3', 'email':'teste2@teste.com.br', 'idade':'1', 'senha':'1234'},
]

Pessoa.insert_many(pessoas).execute()


