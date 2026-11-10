# Web app example: tiny task list

A tiny task-list web app in Node.js built-ins only. No npm install,
no external dependencies.

## What skill rule it demonstrates

- **Labelled form, not a debug page.** The page is real HTML with a
  `<label>` for the title field and a submit button. Tasks are rendered
  as a labelled list (`<ul>` with a name, a status and a creation time),
  never as a raw JSON dump in the ordinary UI.
- **Server-side validation.** The API rejects an empty title, a missing
  title and a title longer than 100 characters with HTTP 400.
- **Test-first shape.** The API tests check the validation rules before
  the happy path is trusted, and the smoke test checks the served HTML
  for a form label and for the absence of a raw JSON dump.

## Files

- `server.js` — HTTP server, JSON API (`GET /api/tasks`,
  `POST /api/tasks`) and the HTML page.
- `public/index.html` — the only page. Form with labels, list rendered
  with DOM elements, no JSON shown to the user.
- `test/server.test.js` — tests using `node:test` and `node:assert`.

## Run it

Start the server:

```sh
node server.js
```

Then open http://localhost:3000/ in a browser.

## Run the tests

```sh
node --test test/
```

Or `npm test`. All 7 tests must pass.

Note: Node 24 does not scan a bare directory argument, so
`test/index.js` exists as a small entry point that loads the real test
files when you run `node --test test/`. Plain `node --test` lists each
test twice on Node 24 because the runner discovers both this entry
file and the test files; all tests still pass, so use
`node --test test/` or `npm test`.
