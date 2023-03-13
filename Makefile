rave: build publish package-install brain-games
raveli: build publish package-install lint brain-games

install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


lint:
	poetry run flake8 brain_games


package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run



