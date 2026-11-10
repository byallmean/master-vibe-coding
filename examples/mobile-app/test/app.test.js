// Tests for the mobile example logic. Node built-ins only:
// node:test plus node:assert. Run with: node --test test/
'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { validateTitle, validateAmount } = require('../src/validation.js');
const { formatVND, formatDateVN } = require('../src/format.js');
const { taskListScreen } = require('../src/screens.js');

test('title validation rejects an empty title', () => {
  assert.match(validateTitle(''), /empty/);
});

test('title validation rejects a whitespace-only title', () => {
  assert.match(validateTitle('   '), /empty/);
});

test('title validation rejects an overlong title', () => {
  assert.match(validateTitle('x'.repeat(101)), /100/);
});

test('title validation accepts a valid title', () => {
  assert.equal(validateTitle('Mua sữa'), null);
});

test('amount validation rejects a negative amount', () => {
  assert.match(validateAmount(-1), /negative/);
});

test('VND formatting adds the dong unit', () => {
  assert.equal(formatVND(25000000), '25.000.000 đồng');
});

test('VND formatting handles zero', () => {
  assert.equal(formatVND(0), '0 đồng');
});

test('VND formatting rejects a negative amount', () => {
  assert.throws(() => formatVND(-5), RangeError);
});

test('date formatting uses Vietnamese day/month/year order', () => {
  assert.equal(formatDateVN(new Date(2026, 10, 11)), '11/11/2026');
});

test('date formatting accepts an ISO string', () => {
  assert.equal(formatDateVN('2026-11-11'), '11/11/2026');
});

test('task list screen form has a labelled title field', () => {
  const field = taskListScreen.form.fields.find((item) => item.id === 'title');
  assert.ok(field, 'title field exists');
  assert.equal(field.label, 'Tên công việc');
  assert.equal(field.required, true);
});
