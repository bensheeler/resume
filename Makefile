.PHONY: build test

build:
	python3 build_resume.py

test:
	python3 -m unittest tests/test_build_resume.py
