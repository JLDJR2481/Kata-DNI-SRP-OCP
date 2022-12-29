from src.dni import DNI
import pytest

# Casos test para comprobar que el DNI es correcto en cuanto a longitud y en cuanto a carácteres.

# Casos test para dnis cortos


@pytest.mark.dni_corto
def test_dni_corto():
    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '4892').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '9').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '4892992').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '4322173').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '194721').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '2947128').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '2504745').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '182646').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '849212').comprobar_long_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '123456').comprobar_long_dni()

# Casos tests para dnis por encima de la longitud reglamentaria


@pytest.mark.dni_largo
def test_dni_largo():
    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '9820183782').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '2847823671264').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '281653273843234').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '4927142124').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '29745249182').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '2504745263').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '81624637247').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '432217312').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '9820183782104826').comprobar_long_dni()

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '18295638291').comprobar_long_dni()

# Casos test para dnis con caracteres alpha-numéricos para detectar un dni erróneo.
# Los casos test tienen la longitud correcta


@pytest.mark.dni_caracteres_incorrectos
def test_dni_caracteres_incorrectos():
    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '2837A212').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        'E2749391').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '182945Y2').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        'P1825482').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        'X1827381').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '3927571Q').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '481693K1').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '5724149I').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '882936W2').comprobar_car_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '1924528Ñ').comprobar_car_dni()


# Casos test mixtos, con errores de longitud o de caracteres. El error de longitud prioriza por encima del error de caracteres
@pytest.mark.dni_mixtos
def test_dni_mixtos():
    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI(
        '432217312').comprobar_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '4322173E').comprobar_dni()

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI(
        '43').comprobar_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        '4322173E').comprobar_dni()

    assert 'Error: Caracteres no aceptados encontrados' == DNI(
        'AYD12837').comprobar_dni()


# Casos test para dnis con longitud y caracteres correctos


@pytest.mark.dni_correcto
def test_dni_correcto():
    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '43221731').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '87654321').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '12345678').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '88328718').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '56271662').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '99326312').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '58493726').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '11458293').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '22183726').comprobar_dni()

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI(
        '43221731').comprobar_dni()
