#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  console.log(body.title);
});
