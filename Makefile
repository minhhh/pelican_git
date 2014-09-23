##

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

clean: # clean
	rm -fr venv

install: # install
	virtualenv venv
	. venv/bin/activate && pip install -r requirements.txt

test:
	. venv/bin/activate && cd pelican_git && py.test --verbose --capture=sys

run: run # run
	. venv/bin/activate && cd blog && make devserver && make regenerate && make stopserver

stop: stop # stop
	. venv/bin/activate && cd blog && make stopserver

flake: # Run flake8 against the repo
	. venv/bin/activate && flake8 pelican_git

publish: # Publish
	. venv/bin/activate && python setup.py publish
