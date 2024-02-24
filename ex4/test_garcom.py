import pytest
from garcom import calcula_gorjeta


def test_gorjeta_valor_despesa_negativo():
    with pytest.raises(ValueError):
        calcula_gorjeta(-1)


def test_gorjeta_valor_despesa_75_00():
    assert calcula_gorjeta(75.00) == (
        pytest.approx(82.50, 0.01), pytest.approx(7.50, 0.01))


def test_gorjeta_valor_despesa_125():
    assert calcula_gorjeta(125) == (pytest.approx(
        137.50, 0.01), pytest.approx(12.50, 0.01))


def test_gorjeta_valor_despesa_350_87():
    assert calcula_gorjeta(350.87) == (pytest.approx(
        385.96, 0.01), pytest.approx(35.09, 0.01))
