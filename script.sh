#!/bin/bash

set -e

echo "Hola desde script"
echo "-----------------------------------------------------------"


if [[ $TRAVIS_PYTHON_VERSION == 3.4 ]]; then 
	echo -e "Python3 \ntodas las sentencias que se quieran \nejecutar con python 3"

fi
if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then 
	echo "Python2 \n todas las sentencias que se quieran \nejecutar con python 2"

	python TestCalculadora.py
	coverage run --branch TestCalculadora.py
	coverage report -m
fi
