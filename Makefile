install:
	poetry install

brain-calc:
	@poetry run brain-calc

brain-games:
	@poetry run brain-games

brain-gcd:
	@poetry run brain-gcd

brain-even:
	@poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall  

lint:
	poetry run flake8 brain_games
