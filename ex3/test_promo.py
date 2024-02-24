import pytest
from promo import calcula_promocao


def test_promo_valor_produto_negativo():
    with pytest.raises(ValueError):
        calcula_promocao(-1, 1)


def test_promo_desconto_negativo():
    with pytest.raises(ValueError):
        calcula_promocao(1, -1)


def test_promo_desconto_maior_que_valor_produto():
    with pytest.raises(ValueError):
        calcula_promocao(1, 2)


def test_promo_valor_produto_500_desconto_50():
    assert calcula_promocao(500.00, 50.00) == pytest.approx(450.00, 0.01)


def test_promo_valor_produto_10500_desconto_500():
    assert calcula_promocao(10500.00, 500.00) == pytest.approx(10000.00, 0.01)


def test_promo_valor_produto_90_desconto_0_80():
    assert calcula_promocao(90.00, 0.80) == pytest.approx(89.20, 0.01)
