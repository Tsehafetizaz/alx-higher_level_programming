#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  const results = body.reduce((acc, task) => {
    if (task.completed) {
      if (acc[task.userId]) {
        acc[task.userId] += 1;
      } else {
        acc[task.userId] = 1;
      }
    }
    return acc;
  }, {});
  console.log(results);
});
