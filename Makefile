PROJECT = rexus
VIRTUALENV = $(shell which virtualenv)
DEVICE_IP = 172.19.19.139
DEVICE_HOSTNAME = rexus.local
DEVICE_USER = pi
DEVICE_PW = raspberry

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

setup_hosts:
	echo "Make sure to run this as sudo"
	echo "${DEVICE_IP}    ${DEVICE_HOSTNAME}" >> /etc/hosts

init_device:
	echo "Installing ssh-copy-id"
	brew install ssh-copy-id
	echo "Installing ssh key to raspberry pi"
	ssh-copy-id pi@${DEVICE_IP}
	echo "Flipping touchscreen to be right side up for stands"
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'sudo echo "lcd_rotate=2" > /boot/config.txt'
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'reboot'

setup_device_python:
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'wget https://bootstrap.pypa.io/get-pip.py'
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'python get-pip.py'
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'pip install virtualenv'

update_device:
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'rm -rf rexus && mkdir rexus'
	scp -r -i ~/.ssh/id_rsa ./rexus ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	scp -r -i ~/.ssh/id_rsa ./Makefile ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	scp -r -i ~/.ssh/id_rsa ./setup.py ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	scp -r -i ~/.ssh/id_rsa ./requirements.txt ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	scp -r -i ~/.ssh/id_rsa ./VERSION ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	scp -r -i ~/.ssh/id_rsa ./LICENSE ${DEVICE_USER}@${DEVICE_IP}:~/rexus/
	ssh -i ~/.ssh/id_rsa ${DEVICE_USER}@${DEVICE_IP} 'cd rexus && make install'

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
