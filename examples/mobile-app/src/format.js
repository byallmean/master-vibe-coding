// Pure formatting helpers for the mobile example.
// Currency uses the dong unit, dates use Vietnamese formatting.
// No React Native import here: plain JavaScript, tested with node:test.
'use strict';

const { validateAmount } = require('./validation.js');

function formatVND(amount) {
  const problem = validateAmount(amount);
  if (problem) {
    throw new RangeError(problem);
  }
  const grouped = new Intl.NumberFormat('vi-VN').format(amount);
  return `${grouped} đồng`;
}

function formatDateVN(value) {
  const date = value instanceof Date ? value : new Date(value);
  if (Number.isNaN(date.getTime())) {
    throw new RangeError('date must be a valid date');
  }
  return new Intl.DateTimeFormat('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  }).format(date);
}

module.exports = { formatVND, formatDateVN };
