def calcular_salario(valor_hora_aula, numero_aulas, percentual_inss):
    if valor_hora_aula < 0:
        raise ValueError('Valor hora aula inválido')
    if numero_aulas < 0:
        raise ValueError('Número de aulas inválido')
    if percentual_inss < 0 or percentual_inss > 100:
        raise ValueError('Percentual INSS inválido')

    liquido = valor_hora_aula * numero_aulas * (1 - percentual_inss / 100)

    return liquido
