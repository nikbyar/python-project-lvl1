rave: build publish package-install
raveli: build publish package-install lint brain-even

install:
	poetry install


brain-games:
	poetry run brain-games


brain-even:
	poetry run brain-even

build:
	poetry build


lint:
	poetry run flake8 brain_games


package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run



