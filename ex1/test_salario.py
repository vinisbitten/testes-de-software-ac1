import pytest
from salario import calcular_salario


def test_salario_valor_hora_negativo():
    with pytest.raises(ValueError):
        calcular_salario(-1, 1, 1)


def test_salario_numero_aulas_negativo():
    with pytest.raises(ValueError):
        calcular_salario(1, -1, 1)


def test_salario_percentual_inss_negativo():
    with pytest.raises(ValueError):
        calcular_salario(1, 1, -1)


def test_salario_percentual_inss_maior_que_100():
    with pytest.raises(ValueError):
        calcular_salario(1, 1, 101)


def test_salario_valor_hora_6_25_numero_aulas_160_percentual_inss_1_3():
    assert calcular_salario(6.25, 160, 1.3) == pytest.approx(987.00, 0.01)


def test_salario_valor_hora_20_5_numero_aulas_240_percentual_inss_1_7():
    assert calcular_salario(20.5, 240, 1.7) == pytest.approx(4836.36, 0.01)


def test_salario_valor_hora_13_9_numero_aulas_200_percentual_inss_6_48():
    assert calcular_salario(13.9, 200, 6.48) == pytest.approx(2599.86, 0.01)
