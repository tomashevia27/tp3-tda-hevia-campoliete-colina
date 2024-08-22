# Trabajo Practico 3: Reducciones, Backtracking, PL, Greedy, Aproximaciones

## Descripción

Este repositorio contiene el Trabajo Práctico 3 de la materia Teoría de Algoritmos - Cátedra Buchwald/Genender - de la Facultad de Ingeniería de la UBA. Este trabajo fue realizado por los alumnos:

- Tomás Hevia
- Manuel Campoliete
- Andrés Colina

El TP no fue realizado en este repositorio, fue realizado aca: https://github.com/manucampoliete/tp3-tda-hevia-campoliete-colina

## Ejecución

Para ejecutar el programa, estando en el directorio del repositorio clonado se debe ingresar en la terminal el comando python3 tp3.py seguido de la ruta relativa del archivo .txt a ejecutar, que debe cumplir con el mismo formato que el especificado por la cátedra, y seguido de la técnica de diseño elegida para resolver el problema, es decir:

`python3 tp3.py <test> <tecnica>`

Los comandos para las técnicas son:

- greedy  (algoritmo de aproximacion propuesto por la catedra)
- greedy2 (algoritmo de aproximacion propio)
- bt
- pl

Por otro lado

- Los tests de la cátedra se encuentran en la carpeta TESTS
- Nuestros tests se encuentran en la carpeta MAS_TESTS, en donde hay 2 subcarpetas: K-Fijo y N-Fijo. En K-Fijo se presentan tests que van de 4_4.txt al 18_4.txt. En N-Fijo se presentan tests que van de 17_2.txt a 17_10.txt
- Si se quiere correr otros tests se debería especificar la ruta correspondiente

Por ejemplo

- Si se quiere correr el test 5_2.txt de la cátedra, utilizando Backtracking como técnica el comando a ejecutar sería:

`python3 tp3.py TESTS/5_2.txt bt`

- Si se quiere correr nuestro test 4_4.txt, utilizando Programación Lineal como técnica el comando a ejecutar sería:

`python3 tp3.py MAS_TESTS/K-Fijo/4_4.txt pl`
