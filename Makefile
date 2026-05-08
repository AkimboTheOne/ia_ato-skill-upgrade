PYTHON ?= python3
VENV ?= .venv
CLI ?= $(VENV)/bin/ato-skill-upgrade

.PHONY: install setup bootstrap doctor validate test

install:
	./scripts/install.sh

setup:
	./scripts/setup.sh

bootstrap:
	cp -n .env.example .env || true
	cp -n config.example.yaml config.yaml || true

doctor:
	@if [ -x "$(CLI)" ]; then \
		"$(CLI)" doctor; \
	else \
		ato-skill-upgrade doctor; \
	fi

validate:
	@if [ -x "$(CLI)" ]; then \
		"$(CLI)" validate; \
	else \
		ato-skill-upgrade validate; \
	fi

test:
	$(PYTHON) -m compileall -q cli
	PYTHONPATH=cli $(PYTHON) -m unittest discover -s tests -q
