# Kata-DNI-SRP-OCP

## **Indice**
- [**Disclaimer**](#disclaimer)
- [**Introducción**](#introducción)
- [**DNIS**](#dni)
  - [**Algoritmo**](#algoritmo-de-letras)
- [**Funcionamiento**](#funcionamiento)
- [**Información extra**](#información-extra)
  
## Disclaimer
Las imágenes que se muestren son imágenes tomadas del documento otorgado por nuestro [tutor](https://github.com/dfleta)

## Introducción
Bienvenido al 2º Kata navideño del curso de Formación Profesional Superior en Desarrollo de Aplicaciones Webs

Este kata se basa en la creación de un asignador de letras para los DNI's de nacionalidad española (Los NIE's no entran en dicho kata)

## DNI
Los DNIS son los Documentos Nacionales de Identidad que otorga el Estado Español a cada ciudadano que haya nacido en España o cuyos padres son españoles y los mismos decidan otorgar la nacionalidad española. Cada DNI es único para cada ciudadano.

Cada DNI está compuesto de una cadena de 8 dígitos más una letra que se le asigna mediante un algoritmo.

### Algoritmo de letras
Antes de empezar, debemos saber que para la asignación de las letras, el Estado tiene una tabla en la cual cada número corresponde a una letra. Se excluyen algunas como la Ñ y la O, para evitar confusiones.
![tabla de letras](https://user-images.githubusercontent.com/115024410/210185121-b3a7902b-b486-4860-ac37-dcb08a68cad7.png)

Tras conocer la tabla de asignación de letras, el algoritmo que asigna la letra es muy simple, aunque tiene ciertos requisitos:

- Primero de todo, la longitud de la cadena sin la letra debe ser de 8 carácteres. Si el primer numero es 0, tambien cuenta como 1 caracter
- Además, solo pueden asignarse letras al final de la cadena. Si el algoritmo detecta un carácter no aceptado (normalmente letras), no se ejecutará dicho algoritmo.

Tras pasar los requisitos, se aplica un algoritmo muy simple, dividir la cadena entre la longitud de la tabla(23). Tras dividir, se recoge el resto y se le asigna la letra correspondiente.

## Funcionamiento
Para ejecutar el codigo, simplemente hay que ejecutar el archivo main.py, ubicado en el fichero src, el cual recoge un input, verifica si cumple los requisitos necesarios para calcular la letra y, si los cumple, otorga la letra correspondiente.

## Información extra
Este kata se ha trabajado y practicado el método TDD (Test Driven Domain), que consiste en la programación basandose en casos test previamente planteados, y las clases, siendo una introducción y práctica de las mismas






