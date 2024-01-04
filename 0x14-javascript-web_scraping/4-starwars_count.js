#!/usr/bin/node
// A script that prints the number of movies where
// the character "Wedge Antillies" is present

// Include request module
const request = require('request');

// url/endpoint variable
const url = process.argv[2];

// Initialize the counter
let counter = 0;

// Use request to fetch the data
request(url, function (err, response, body) {
  // Handle error
  if (err) console.log(err);
  // Printing th number of movies
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; i++) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; j++) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
