// Tiny task-list web app. Node.js built-ins only, no dependencies.
// Serves one HTML page plus a small JSON API.
// Skill rules demonstrated: labelled form (no debug page), input
// validation on the server, tasks rendered as a labelled list,
// never raw JSON in the ordinary UI.
'use strict';

const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const MAX_TITLE_LENGTH = 100;

function createApp() {
  const tasks = [];
  let nextId = 1;

  function sendJson(res, status, obj) {
    const body = JSON.stringify(obj);
    res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(body);
  }

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

  const server = http.createServer((req, res) => {
    const url = new URL(req.url, 'http://localhost');

    if (req.method === 'GET' && url.pathname === '/') {
      const htmlPath = path.join(__dirname, 'public', 'index.html');
      fs.readFile(htmlPath, 'utf8', (err, html) => {
        if (err) {
          res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
          res.end('Could not load page');
          return;
        }
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(html);
      });
      return;
    }

    if (req.method === 'GET' && url.pathname === '/api/tasks') {
      sendJson(res, 200, { tasks });
      return;
    }

    if (req.method === 'POST' && url.pathname === '/api/tasks') {
      let raw = '';
      req.on('data', (chunk) => { raw += chunk; });
      req.on('end', () => {
        let body;
        try {
          body = JSON.parse(raw);
        } catch {
          sendJson(res, 400, { error: 'body must be valid JSON' });
          return;
        }
        const problem = validateTitle(body && body.title);
        if (problem) {
          sendJson(res, 400, { error: problem });
          return;
        }
        const task = {
          id: nextId,
          title: body.title.trim(),
          done: false,
          createdAt: new Date().toISOString(),
        };
        nextId += 1;
        tasks.push(task);
        sendJson(res, 201, { task });
      });
      return;
    }

    sendJson(res, 404, { error: 'not found' });
  });

  return { server, tasks };
}

if (require.main === module) {
  const port = Number(process.env.PORT || 3000);
  const { server } = createApp();
  server.listen(port, () => {
    console.log(`Task app listening at http://localhost:${port}/`);
  });
}

module.exports = { createApp, MAX_TITLE_LENGTH };
