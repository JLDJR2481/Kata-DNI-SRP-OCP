from src.dni import DNI
import pytest

# Casos test para comprobar que el DNI es correcto en cuanto a longitud y en cuanto a carácteres.

# Casos test para dnis cortos


@pytest.mark.dni_corto
def test_dni_corto():
    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '4892')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '9')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '4892992')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '4322173')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '194721')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '2947128')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '2504745')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '182646')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '849212')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '123456')

# Casos tests para dnis por encima de la longitud reglamentaria


@pytest.mark.dni_largo
def test_dni_largo():
    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '9820183782')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '2847823671264')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '281653273843234')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '4927142124')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '29745249182')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '2504745263')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '81624637247')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '432217312')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '9820183782104826')

    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_long_dni(
        '18295638291')

# Casos test para dnis con caracteres alpha-numéricos para detectar un dni erróneo.
# Los casos test tienen la longitud correcta


@pytest.mark.dni_caracteres_incorrectos
def test_dni_caracteres_incorrectos():
    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '2837A212')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        'E2749391')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '182945Y2')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        'P1825482')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        'X1827381')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '3927571Q')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '481693K1')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '5724149I')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '882936W2')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_car_dni(
        '1924528Ñ')


# Casos test mixtos, con errores de longitud o de caracteres. El error de longitud prioriza por encima del error de caracteres
@pytest.mark.dni_mixtos
def test_dni_mixtos():
    assert 'Error: El DNI está por encima de la longitud reglamentaria' == DNI.comprobar_dni(
        '432217312')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_dni(
        '4E2A173E')

    assert 'Error: El DNI está por debajo de la longitud reglamentaria' == DNI.comprobar_dni(
        '43')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_dni(
        '4322173E')

    assert 'Error: Caracteres no aceptados encontrados' == DNI.comprobar_dni(
        'AYD12837')


# Casos test para dnis con longitud y caracteres correctos


@pytest.mark.dni_correcto
def test_dni_correcto():
    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '43221731')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '87654321')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '12345678')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '88328718')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '56271662')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '99326312')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '58493726')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '11458293')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '22183726')

    assert 'DNI aceptado: Longitud y caracteres correctos' == DNI.comprobar_dni(
        '43221731')
