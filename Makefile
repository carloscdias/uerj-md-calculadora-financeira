default: run

install_dependencies:
	pip install -r requirements.txt

run: install_dependencies
	python calculadora-financeira.py
