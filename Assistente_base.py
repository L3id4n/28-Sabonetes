soja = {
    "temperatura_min": 20,
    "temperatura_max": 30,
    "chuva_ciclo_min": 450,
    "chuva_ciclo_max": 800,
    "ph_solo_min": 5.5,
    "ph_solo_max": 6.5,
    "tempo_min": 100,
    "tempo_max": 160,
    "drenagem": "bom"
}                                               

milho = {
    "temperatura_min": 18,
    "temperatura_max": 32,
    "chuva_ciclo_min": 500,
    "chuva_ciclo_max": 800,
    "ph_solo_min": 5.5,
    "ph_solo_max": 7,
    "tempo_min": 90,
    "tempo_max": 150,
    "nutrientes": "alto"    
}

trigo = {
    "temperatura_min": 15,
    "temperatura_max": 25,
    "chuva_ciclo_min": 450,
    "chuva_ciclo_max": 650,
    "ph_solo_min": 5.5,
    "ph_solo_max": 6.5,
    "tempo_min": 110,
    "tempo_max": 150,
    "clima": "ameno"     
}

plantas = input("Digite qual planta deseja plantar [milho/soja/trigo]: ")

if plantas == "soja":
        temperatura = float(input("Temperatura média (°C): "))
        chuva = float(input("Previsão de chuva no ciclo (mm): "))
        ph = float(input("pH do solo: "))
        fertilidade = input("O solo é fértil? [sim/não]: ").lower()
        
        pontos = 0
        
        if soja["temperatura_min"] <= temperatura <= soja["temperatura_max"]:
            pontos += 25
        
        if soja["chuva_ciclo_min"] <= chuva <= soja["chuva_ciclo_max"]:
            pontos += 25
            
        if soja["ph_solo_min"] <= ph <= soja["ph_solo_max"]:
            pontos += 25
        
        if fertilidade == "sim":
            pontos += 25
            
        print(f"Compatibilidade: {pontos}%")

if plantas == "milho":
        temperatura = float(input("Temperatura média (°C): "))
        chuva = float(input("Previsão de chuva no ciclo (mm): "))
        ph = float(input("pH do solo: "))
        fertilidade = input("O solo é fértil? [sim/não]: ").lower()
        
        pontos = 0
        
        if milho["temperatura_min"] <= temperatura <= milho["temperatura_max"]:
            pontos += 25
        
        if milho["chuva_ciclo_min"] <= chuva <= milho["chuva_ciclo_max"]:
            pontos += 25
            
        if milho["ph_solo_min"] <= ph <= milho["ph_solo_max"]:
            pontos += 25
        
        if fertilidade == "sim":
            pontos += 25
            
        print(f"Compatibilidade: {pontos}%")
            
if plantas == "trigo":
        temperatura = float(input("Temperatura média (°C): "))
        chuva = float(input("Previsão de chuva no ciclo (mm): "))
        ph = float(input("pH do solo: "))
        fertilidade = input("O solo é fértil? [sim/não]: ").lower()
        
        pontos = 0
        
        if trigo["temperatura_min"] <= temperatura <= trigo["temperatura_max"]:
            pontos += 25
        
        if trigo["chuva_ciclo_min"] <= chuva <= trigo["chuva_ciclo_max"]:
            pontos += 25
            
        if trigo["ph_solo_min"] <= ph <= trigo["ph_solo_max"]:
            pontos += 25
        
        if fertilidade == "sim":
            pontos += 25
            
        print(f"Compatibilidade: {pontos}%")

