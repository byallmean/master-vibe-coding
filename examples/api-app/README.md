# API app example: tiny JSON API

A tiny JSON API in Python standard library only. No pip install,
no external dependencies.

## What skill rule it demonstrates

- **Server-side input validation.** Creating an item rejects an empty
  name, a missing name and a name longer than 100 characters with
  HTTP 400.
- **Never trust the client: mass-assignment protection.** Only the
  allowlisted fields `name` and `note` are ever stored. Extra fields
  in the request body such as `is_admin`, `role` or `credits` are
  ignored, not stored.
- **Auth secret from the environment, never hardcoded.** The protected
  endpoint `GET /protected` requires a bearer value read from the
  `API_BEARER` environment variable (or passed to `create_server`).
  There is no secret value anywhere in the code. Set it before
  running the server, for example:
  `API_BEARER=<your-value> python3 app.py`
- **Rate limiting.** `POST /login` allows at most 5 attempts per IP
  per 60 seconds and answers 429 afterwards.

## Files

- `app.py` — HTTP server and all endpoints.
- `test/test_app.py` — tests using Python `unittest`.

## Run it

```sh
API_BEARER=<your-value> python3 app.py
```

Then `GET http://127.0.0.1:8000/health` answers `{"ok": true}`.

## Run the tests

```sh
python3 -m unittest discover -s test -v
```

All 10 tests must pass. The tests pass their own bearer value to
`create_server`, so no environment variable is needed to run them.
