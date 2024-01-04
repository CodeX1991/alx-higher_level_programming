#!/usr/bin/node
// A script that display prints the title of a Star Wars movie
// where the episode number matches a given integer

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
    // Printing status code
    body = JSON.parse(body);
    console.log(body.title);
  }
});
