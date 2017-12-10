PROJECT = rexus

VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
	VIRTUALENV = /usr/local/python/bin/virtualenv
endif

venv:
	virtualenv venv

flake: venv ## Check PEP8
	. venv/bin/activate; \
	flake8 --max-line-length=100 rexus

test-install: venv
	. venv/bin/activate; pip install -r tests/requirements.txt

unit-test: venv
	. venv/bin/activate; python -m unittest discover tests/

check: venv flake

test: test-install
	. venv/bin/activate; py.test tests/

install: venv
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install --editable .

run_gui: install
	. venv/bin/activate && \
	cd rexus/gui && \
	export FLASK_APP=__init__.py && \
	export FLASK_DEBUG=1 && \
	python -m flask run

clean:
	rm -rf venv
	rm -rf $(PROJECT)/packages
	rm -rf tmp
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -f $(PROJECT)/*,cover
	rm -f $(PROJECT)/*.pyc
	rm -f tests/*.pyc
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
