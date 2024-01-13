#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Include request module
const request = require('request');

// url/endpoint variable
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

// Use request to fetch the data
request(url, function (err, response, body) {
  // Printing the error if occurred
  if (err) {
    console.log(err);
  } else {
    // Printing characters
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], function (_cErr, _cRes, _cBody) {
        console.log(JSON.parse(_cBody).name);
      });
    }
  }
});
