#!/usr/bin/node
const request = require('request');
const async = require('async'); // Ensure to install async via npm

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, film) => {
  if (err) {
    return console.error(err);
  }

  async.mapSeries(film.characters, (characterUrl, callback) => {
    request(characterUrl, { json: true }, (err, res, character) => {
      if (err) {
        return callback(err);
      }
      callback(null, character.name);
    });
  }, (err, results) => {
    if (err) {
      console.error(err);
    } else {
      results.forEach(name => console.log(name));
    }
  });
});
