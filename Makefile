rave: build publish package-install
raveli: build publish package-install lint brain-prime

install:
	poetry install


brain-games:
	poetry run brain-games


brain-even:
	poetry run brain-even


brain-calc:
	poetry run brain-calc


brain-gcd:
	poetry run brain-gcd


brain-progression:
	poetry run brain-progression


brain-prime:
	poetry run brain-prime


build:
	poetry build


lint:
	poetry run flake8 brain_games


package-install:
	python3 -m pip install --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run



