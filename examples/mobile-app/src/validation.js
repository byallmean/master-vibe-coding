// Pure form validation logic for the mobile example.
// No React Native import here: this module is plain JavaScript so its
// tests run with node:test and no build step or device.
'use strict';

const MAX_TITLE_LENGTH = 100;

function validateTitle(value) {
  if (typeof value !== 'string') {
    return 'title must be a string';
  }
  const title = value.trim();
  if (title.length === 0) {
    return 'title must not be empty';
  }
  if (title.length > MAX_TITLE_LENGTH) {
    return 'title must be at most 100 characters';
  }
  return null;
}

function validateAmount(value) {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    return 'amount must be a finite number';
  }
  if (value < 0) {
    return 'amount must not be negative';
  }
  if (!Number.isInteger(value)) {
    return 'amount must be a whole number of dong';
  }
  return null;
}

module.exports = { validateTitle, validateAmount, MAX_TITLE_LENGTH };
