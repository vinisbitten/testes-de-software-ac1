def calcula_gorjeta(valor_despesa):
    if valor_despesa < 0:
        raise ValueError('Valor da despesa inválido')

    valor_gorjeta = valor_despesa * 0.1
    valor_total = valor_despesa + valor_gorjeta

    return valor_total, valor_gorjeta
