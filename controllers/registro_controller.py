import re
from models.models import db, Registro

def validar_tempo(tempo):
    """ Valida o formato do tempo no formato MM:SS:MM """
    padrao_tempo = re.compile(r"^\d{2}:\d{2}:\d{2}$")
    return padrao_tempo.match(tempo) is not None

def adicionar_registro(nomePiloto, tempo, pista):
    """ Adiciona um novo registro ao banco de dados """
    if nomePiloto and tempo and pista and validar_tempo(tempo):
        novo_registro = Registro(nomePiloto=nomePiloto, tempo=tempo, pista=pista)
        db.session.add(novo_registro)
        db.session.commit()
        return True
    return False

def obter_registros():
    """ Retorna todos os registros do banco de dados """
    return Registro.query.all()

def limpar_registros():
    """ Remove todos os registros do banco de dados """
    db.session.query(Registro).delete()
    db.session.commit()

def deletar_registro(id):
    """ Remove um registro do banco de dados """
    registro = Registro.query.get(id)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        return True
    return False
