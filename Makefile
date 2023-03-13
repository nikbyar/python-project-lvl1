rave: build publish package-install brain-games

install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run



