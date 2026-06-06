from flask import Flask, render_template, request

app = Flask(__name__)

soja = {
    "temperatura_min": 20,
    "temperatura_max": 30,
    "chuva_ciclo_min": 450,
    "chuva_ciclo_max": 800,
    "ph_solo_min": 5.5,
    "ph_solo_max": 6.5,
    "drenagem": "boa"
}

milho = {
    "temperatura_min": 18,
    "temperatura_max": 32,
    "chuva_ciclo_min": 500,
    "chuva_ciclo_max": 800,
    "ph_solo_min": 5.5,
    "ph_solo_max": 7,
    "nutrientes": "alto"
}

trigo = {
    "temperatura_min": 15,
    "temperatura_max": 25,
    "chuva_ciclo_min": 450,
    "chuva_ciclo_max": 650,
    "ph_solo_min": 5.5,
    "ph_solo_max": 6.5,
    "clima": "ameno"
}


def calcular_pontos(
    planta,
    temperatura,
    chuva,
    ph,
    fertilidade,
    drenagem,
    nutrientes,
    clima
):
    pontos = 0

    if planta["temperatura_min"] <= temperatura <= planta["temperatura_max"]:
        pontos += 20

    if planta["chuva_ciclo_min"] <= chuva <= planta["chuva_ciclo_max"]:
        pontos += 20

    if planta["ph_solo_min"] <= ph <= planta["ph_solo_max"]:
        pontos += 20

    if fertilidade == "sim":
        pontos += 20

    if "drenagem" in planta:
        if drenagem == planta["drenagem"]:
            pontos += 20

    elif "nutrientes" in planta:
        if nutrientes == planta["nutrientes"]:
            pontos += 20

    elif "clima" in planta:
        if clima == planta["clima"]:
            pontos += 20

    return pontos


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():

    temperatura = float(request.form["temperatura"])
    chuva = float(request.form["chuva"])
    ph = float(request.form["ph"])

    fertilidade = request.form["fertilidade"]
    drenagem = request.form["drenagem"]
    nutrientes = request.form["nutrientes"]
    clima = request.form["clima"]

    resultado_soja = calcular_pontos(
        soja,
        temperatura,
        chuva,
        ph,
        fertilidade,
        drenagem,
        nutrientes,
        clima
    )

    resultado_milho = calcular_pontos(
        milho,
        temperatura,
        chuva,
        ph,
        fertilidade,
        drenagem,
        nutrientes,
        clima
    )

    resultado_trigo = calcular_pontos(
        trigo,
        temperatura,
        chuva,
        ph,
        fertilidade,
        drenagem,
        nutrientes,
        clima
    )
    resultados = {
        "Soja": resultado_soja,
        "Milho": resultado_milho,
        "Trigo": resultado_trigo
    }
    
    maior_pontuacao = max(resultados.values())
    
    melhores_plantas = []

    for planta, pontos in resultados.items():
        if pontos == maior_pontuacao:
            melhores_plantas.append(planta)
        
    ranking = sorted(
        resultados.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return render_template(
    "resultado.html",
    ranking=ranking,
    melhores_plantas=melhores_plantas,
    maior_pontuacao=maior_pontuacao,
    resultados=resultados
    )


if __name__ == "__main__":
    app.run(debug=True)