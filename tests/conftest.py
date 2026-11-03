"""Keep every test isolated from the tracked historical database."""
import pytest

from movies.movie import Movie


@pytest.fixture(autouse=True)
def isolated_database(tmp_path, monkeypatch):
    database = str(tmp_path / "movies-test.db")
    monkeypatch.setenv("DATABASE_NAME", database)
    Movie.create_table(database)
