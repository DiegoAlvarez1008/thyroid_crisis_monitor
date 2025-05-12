def evaluar_parametros(temp, fc):
    # Puedes ajustar estos valores luego
    if temp >= 40.0 or fc >= 130:
        return "critico"
    elif temp >= 38.5 or fc >= 100:
        return "preocupante"
    else:
        return "normal"
