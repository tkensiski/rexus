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

check: venv flake unit-test

analysis:
	. venv/bin/activate; flake8 $(PROJECT)/*.py tests/*.py

init:
	pip install -r requirements.txt;

test: test-install
	. venv/bin/activate; py.test tests/

install: venv
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install --editable .

develop: install

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

zip: $(PROJECT).zip

$(PROJECT).zip: clean install
	rm -rf build ; \
	mkdir build ; \
	cp -R marvin/* build/ ; \
	cp -R venv/lib/python2.7/site-packages/* build/ ; \
	pushd build/ ; \
	zip -x '*.pyc' -r ../marvin.zip .
