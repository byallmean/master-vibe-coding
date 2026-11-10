// Tests for the tiny task-list web app. Node built-ins only:
// node:test plus node:assert. Run with: node --test test/
'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { createApp } = require('../server.js');

let baseUrl;
const { server } = createApp();

test.before(async () => {
  await new Promise((resolve) => server.listen(0, resolve));
  baseUrl = `http://127.0.0.1:${server.address().port}`;
});

test.after(() => new Promise((resolve) => server.close(resolve)));

test('home page returns HTML with a labelled form', async () => {
  const res = await fetch(`${baseUrl}/`);
  assert.equal(res.status, 200);
  assert.match(res.headers.get('content-type'), /text\/html/);
  const html = await res.text();
  assert.match(html, /<form/);
  assert.match(html, /<label for="title">/);
  assert.match(html, /Tên công việc/);
});

test('home page shows no raw JSON dump', async () => {
  const res = await fetch(`${baseUrl}/`);
  const html = await res.text();
  assert.doesNotMatch(html, /"tasks"\s*:/);
  assert.doesNotMatch(html, /\{\s*"id"\s*:/);
});

test('creating a task with a valid title works and it appears in the list', async () => {
  const created = await fetch(`${baseUrl}/api/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: 'Mua sữa' }),
  });
  assert.equal(created.status, 201);
  const createdBody = await created.json();
  assert.equal(createdBody.task.title, 'Mua sữa');
  assert.equal(createdBody.task.done, false);

  const listed = await fetch(`${baseUrl}/api/tasks`);
  assert.equal(listed.status, 200);
  const listedBody = await listed.json();
  assert.ok(Array.isArray(listedBody.tasks));
  assert.ok(listedBody.tasks.some((task) => task.title === 'Mua sữa'));
});

test('creating a task with an empty title is rejected', async () => {
  const res = await fetch(`${baseUrl}/api/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: '   ' }),
  });
  assert.equal(res.status, 400);
  const body = await res.json();
  assert.match(body.error, /empty/);
});

test('creating a task with a missing title is rejected', async () => {
  const res = await fetch(`${baseUrl}/api/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({}),
  });
  assert.equal(res.status, 400);
});

test('creating a task with an overlong title is rejected', async () => {
  const res = await fetch(`${baseUrl}/api/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: 'x'.repeat(101) }),
  });
  assert.equal(res.status, 400);
  const body = await res.json();
  assert.match(body.error, /100/);
});

test('unknown route returns 404 JSON', async () => {
  const res = await fetch(`${baseUrl}/no-such-route`);
  assert.equal(res.status, 404);
});
