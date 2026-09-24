install:
	uv sync

VD-games:
	uv run vd-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check VD_games --ignore N999
