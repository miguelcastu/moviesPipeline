# Movies API — Flask / SQLite Backend Exercise

A historical backend exercise separating HTTP handlers, command/query objects
and SQLite persistence. It creates and lists movie records and retrieves a movie
by ID, with pytest tests and JSON Schema response checks.

[Engineering portfolio](https://github.com/miguelcastu/miguelcastu)
· [Project directory](https://github.com/miguelcastu/miguelcastu/blob/main/PROJECTS.md)

## Implementation

```text
Flask routes → command/query objects → Pydantic Movie → SQLite
```

- [web_app.py](web_app.py): POST `/create-movie/`, GET `/movie/<movie_id>/`
  and GET `/movie-list/`.
- [movie_commands.py](movies/movie_commands.py): creation and query operations.
- [movie.py](movies/movie.py): model and SQLite access, using parameterized SQL.
- [tests/](tests/): model, command and API response tests.

## Local setup

With Python 3.12 and uv, from the repository root:

```shell
uv venv --python 3.12
uv pip install -r requirements-dev.txt
uv run --no-project python -c "from movies.movie import Movie; Movie.create_table('local-movies.db')"
```

Set `DATABASE_NAME=local-movies.db` in your shell, then run:

```shell
uv run --no-project flask --app web_app run --host 127.0.0.1
uv run --no-project python -m pytest -q
```

On PowerShell set the variable with `$env:DATABASE_NAME = "local-movies.db"`.
The explicit database avoids modifying the tracked historical `movies.db`.
Tests use per-test temporary databases, independent of the application database.
The requirements file pins the direct packages used for the verified workflow;
it is not a complete transitive lockfile.

## Scope and limitations

This is a local learning API without authentication or a production deployment
configuration. Missing-record and invalid-request error contracts need improvement.
The original GitLab scripts remain historical material; an echo about Heroku is
not evidence of a deployment. GitHub Actions runs local pytest only and has
read-only repository permissions. Database and OS-generated historical files are
preserved pending a separate cleanup review.
