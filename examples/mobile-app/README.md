# Mobile app example: React Native / Expo-style skeleton

A React Native / Expo-style project skeleton with **no build
dependency**. The `src/` folder holds pure logic modules plus a screen
layout described as data. There is no runnable UI in this example.

## Honest note about what is not covered here

UI rendering is **not** covered here. Rendering these screens needs a
device or an emulator with an Expo / React Native toolchain, which this
example deliberately does not require. What is covered and tested is
the logic a real screen would use: form validation, currency
formatting and date formatting.

## What skill rule it demonstrates

- **Validation before submit.** `validateTitle` rejects an empty title
  and a title longer than 100 characters, the same rule as the web
  example, so the rule is shared and tested in both places.
- **Currency with its unit.** `formatVND` renders amounts as
  `25.000.000 đồng`, never as a bare number and never with the
  forbidden `k` shorthand.
- **Dates in the user's language.** `formatDateVN` renders dates as
  `11/11/2026` in Vietnamese day/month/year order.
- **Layout as data.** `src/screens.js` describes the task list screen
  as plain data: a header, a form whose title field has a label, and
  a list whose items show a name, a status and a creation date. No raw
  JSON is shown to the user in the real app.

## Files

- `src/validation.js` — pure validation logic.
- `src/format.js` — VND currency and Vietnamese date formatting.
- `src/screens.js` — screen layout described as data.
- `test/app.test.js` — tests using `node:test` and `node:assert`.

## Run the tests

```sh
node --test test/
```

Or `npm test`. All 11 tests must pass.

Note: Node 24 does not scan a bare directory argument, so
`test/index.js` exists as a small entry point that loads the real test
files when you run `node --test test/`. Plain `node --test` lists each
test twice on Node 24 because the runner discovers both this entry
file and the test files; all tests still pass, so use
`node --test test/` or `npm test`.
