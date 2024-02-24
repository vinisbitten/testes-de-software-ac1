def calcula_promocao(valor_produto, desconto):
    if valor_produto < 0:
        raise ValueError('Valor do produto inválido')
    if desconto < 0:
        raise ValueError('Valor do desconto inválido')
    if desconto > valor_produto:
        raise ValueError('Valor do desconto maior que o valor do produto')

    novo_valor = valor_produto - desconto

    return novo_valor
