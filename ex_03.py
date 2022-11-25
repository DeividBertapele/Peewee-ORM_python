from ex_01 import Nota, Grupo, Pessoa


nota = Nota.select().where(Nota.titulo == 'Blah').get()
grupo = Grupo.select().where(Grupo.nome == 'Python').get()

# Alterar valores
nota = Nota.select().where(Nota.titulo == 'Blah').get()
nota.grupo = grupo
nota.save()


notas_rosas = (
    Nota.select()
    .join(Grupo)
    .where(Grupo.nome == 'Python')
    .get()
)