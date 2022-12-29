from src.letras import Letras
import pytest


@pytest.mark.letraCorrecta
def test_letras_correctas():
    assert 'Z' == Letras(66582415).calcularLetra()
    assert 'F' == Letras(86261461).calcularLetra()
    assert 'V' == Letras('07716908').calcularLetra()
    assert 'E' == Letras(34737037).calcularLetra()
    assert 'Q' == Letras(43221731).calcularLetra()
    assert 'Q' == Letras(49640019).calcularLetra()
    assert 'P' == Letras(93835983).calcularLetra()
    assert 'Z' == Letras(71874416).calcularLetra()
    assert 'T' == Letras(95225497).calcularLetra()
    assert 'D' == Letras(57984320).calcularLetra()
    assert 'M' == Letras(59105244).calcularLetra()
    assert 'E' == Letras(63741486).calcularLetra()
    assert 'K' == Letras(33134166).calcularLetra()
    assert 'F' == Letras('08492067').calcularLetra()
    assert 'L' == Letras('09070460').calcularLetra()


@pytest.mark.letraIncorrecta
def test_letras_incorrectas():
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        27381).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        11).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        999203).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        9283121).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        888439).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        10).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        0).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        38293).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        99128).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        83612).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        1).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        2).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        293984).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        4839201).calcularLetra()
    assert 'El DNI no cumple la longitud obligatoria de 8 digitos' == Letras(
        4832).calcularLetra()
