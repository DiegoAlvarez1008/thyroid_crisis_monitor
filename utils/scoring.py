def calcular_puntaje(temp, fc, test_score):
    # Escala simulada tipo Burch-Wartofsky
    puntaje = 0
    if temp >= 38.5:
        puntaje += 10
    if fc >= 100:
        puntaje += 10
    puntaje += test_score  # Resultado del test cognitivo
    return puntaje
