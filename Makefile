install:
	poetry install

brain-games:
	poetry run python -m brain_games.scripts.brain_games

brain-even:
	poetry run python -m brain_games.scripts.brain_even

brain-calc:
	poetry run python -m brain_games.scripts.brain_calc

brain-gcd:
	poetry run python -m brain_games.scripts.brain_gcd

brain-progression:
	poetry run python -m brain_games.scripts.brain_progression

brain-prime:
	poetry run python -m brain_games.scripts.brain_prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
