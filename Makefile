PYENV=.env-arm64
PYTHON=source $(PYENV)/bin/activate && python


setup: $(PYENV)/.env_created
	$(PYTHON) -m pip install -r requirements.txt


venv: $(PYENV)/.venv_created

$(PYENV)/.venv_created:
		python3.12 -m venv $(PYENV)
		touch $@

$(PYENV)/.deps_installed: requirements.txt
		$(PYTHON) -m pip install -r $^
		touch $@

install_deps: $(PYENV)/.deps_installed
.PHONY: install_deps

setup: venv install_deps
.PHONY: setup

run:
	$(PYTHON) app.py
