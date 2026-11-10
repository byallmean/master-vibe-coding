// Entry point so `node --test test/` works on Node 24, which does not
// scan a bare directory argument: the directory resolves to this file,
// which loads the real test files (they register their tests with
// node:test when required). Use `node --test test/` or `npm test`.
// Note: plain `node --test` lists each test twice on Node 24 because
// the runner discovers both this entry file and the test files.
'use strict';

require('./server.test.js');
