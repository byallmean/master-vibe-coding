// Entry point so `node --test test/` works on Node 24, which does not
// scan a bare directory argument. Running `node --test test/` loads
// this file, which loads the real test files (they register their
// tests with node:test when required). `node --test` on its own
// discovers app.test.js directly, so this file is only a shim.
'use strict';

require('./app.test.js');
