# Gen-AI-Assignment-22btrcb041

## Quickstart
1. Create and activate venv
2. Install: `pip install -e .[dev]`
3. Copy `.env.example` to `.env`
4. Run API: `uvicorn src.app.main:app --reload`
5. Docs: open http://127.0.0.1:8000/docs

## Scripts
- Lint: `ruff check .`
- Type-check: `mypy src`
- Test: `pytest -q`

## Migrations
- Init: `alembic init alembic`
- Generate: `alembic revision --autogenerate -m "init"`
- Upgrade: `alembic upgrade head`
