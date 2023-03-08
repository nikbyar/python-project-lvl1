install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


package-install:
	python3 -m pip install dist/*.whl

publish:
	poetry publish --dry-run


