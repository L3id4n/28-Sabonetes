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
    "ph_solo_max": 7.0,
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


def calcular_pontos(planta, temperatura, chuva, ph,
                     fertilidade, drenagem,
                     nutrientes, clima):

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


print("=== Assistente Agrícola ===")

temperatura = float(input("Temperatura média (°C): "))
chuva = float(input("Previsão de chuva no ciclo (mm): "))
ph = float(input("pH do solo: "))
fertilidade = input("Solo fértil? [sim/não]: ").lower()

drenagem = input("Drenagem do solo [ruim/boa]: ").lower()
nutrientes = input("Nível de nutrientes [baixo/medio/alto]: ").lower()
clima = input("Clima da região [frio/ameno/quente]: ").lower()


resultado_soja = calcular_pontos(
    soja, temperatura, chuva, ph,
    fertilidade, drenagem,
    nutrientes, clima
)

resultado_milho = calcular_pontos(
    milho, temperatura, chuva, ph,
    fertilidade, drenagem,
    nutrientes, clima
)

resultado_trigo = calcular_pontos(
    trigo, temperatura, chuva, ph,
    fertilidade, drenagem,
    nutrientes, clima
)


print("\n=== RESULTADOS ===")
print(f"Soja: {resultado_soja}%")
print(f"Milho: {resultado_milho}%")
print(f"Trigo: {resultado_trigo}%")


resultados = {
    "Soja": resultado_soja,
    "Milho": resultado_milho,
    "Trigo": resultado_trigo
}

melhor_planta = max(resultados, key=resultados.get)

print(f"\n Melhor opção: {melhor_planta}")
print(f"Compatibilidade: {resultados[melhor_planta]}%")