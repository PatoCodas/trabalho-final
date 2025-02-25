from flask import Blueprint, render_template, request, redirect, url_for
from controllers import adicionar_registro, obter_registros, limpar_registros, deletar_registro

bp = Blueprint('routes', __name__)

@bp.route('/', methods=["GET", "POST"])
def principal():
    # """ Página principal com listagem e formulário """
    if request.method == "POST":
        if 'deletar' in request.form:
            deletar_pista = request.form['deletar']
            deletar_registro(deletar_pista)
            return redirect(url_for('routes.principal'))
        elif 'nomePiloto' in request.form:
            nomePiloto = request.form.get("nomePiloto")
            tempo = request.form.get("tempo")
            pista = request.form.get("pista")
            if adicionar_registro(nomePiloto, tempo, pista):
                return redirect(url_for('routes.principal'))
            else:
                return "Formato de tempo inválido! Use MM:SS:MM", 400

    registros = obter_registros()
    return render_template("index.html", registros=registros)


@bp.route('/limpar')
def limpar_banco():
    """ Limpa todos os registros do banco """
    limpar_registros()
    return redirect(url_for('routes.principal'))
