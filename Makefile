.PHONY: develop

virtualenv:
	virtualenv virtualenv

develop: virtualenv
	source virtualenv/bin/activate && pip install -r requirements.txt

