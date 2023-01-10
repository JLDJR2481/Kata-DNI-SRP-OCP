from src.tabla import Tabla
import pytest


@pytest.mark.letra_correcta
def test_letras_correctas():
    assert 'Z' == Tabla.calcular_letra(66582415)

    assert 'F' == Tabla.calcular_letra(86261461)

    assert 'V' == Tabla.calcular_letra('07716908')

    assert 'E' == Tabla.calcular_letra(34737037)

    assert 'Q' == Tabla.calcular_letra(43221731)

    assert 'Q' == Tabla.calcular_letra(49640019)

    assert 'P' == Tabla.calcular_letra(93835983)

    assert 'Z' == Tabla.calcular_letra(71874416)

    assert 'T' == Tabla.calcular_letra(95225497)

    assert 'D' == Tabla.calcular_letra(57984320)

    assert 'M' == Tabla.calcular_letra(59105244)

    assert 'E' == Tabla.calcular_letra(63741486)

    assert 'K' == Tabla.calcular_letra(33134166)

    assert 'F' == Tabla.calcular_letra('08492067')

    assert 'L' == Tabla.calcular_letra('09070460')


@pytest.mark.letra_incorrecta
def test_letras_incorrectas():
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        27381)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        11)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        999203)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        9283121)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        888439)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        10)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        0)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        38293)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        99128)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        83612)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        1)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        2)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        293984)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        4839201)

    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Tabla.calcular_letra(
        4832)
