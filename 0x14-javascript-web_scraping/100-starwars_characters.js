#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  const characters = body.characters;
  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error(err);
      } else {
        console.log(body.name);
      }
    });
  });
});
