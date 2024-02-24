import pytest
from desconto import calcular_desconto


def test_desconto_valor_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(-1)


def test_desconto_valor_100():
    assert calcular_desconto(100) == (
        pytest.approx(91.00, 0.01), pytest.approx(9.00, 0.01))


def test_desconto_valor_1500():
    assert calcular_desconto(1500) == (
        pytest.approx(1365.00, 0.01), pytest.approx(135.00, 0.01))


def test_desconto_valor_60000():
    assert calcular_desconto(60000) == (
        pytest.approx(54600.00, 0.01), pytest.approx(5400.00, 0.01))
