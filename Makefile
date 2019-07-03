##

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

install: # install
	pipenv install --dev

test: # unit test
	cd pelican_git && pipenv run py.test --verbose --capture=sys

clean: # clean build
	rm -frv dist build pelican_git.egg-info

run: run # run
	cd blog && pipenv run make devserver PORT=8080 && pipenv run make regenerate && pipenv run make stopserver

stop: stop # stop
	cd blog && pipenv run make stopserver

flake: # Run flake8 against the repo
	pipenv run flake8 pelican_git

publish: # Publish
	pipenv run python setup.py sdist bdist_wheel
	pipenv run twine upload dist/* --verbose
