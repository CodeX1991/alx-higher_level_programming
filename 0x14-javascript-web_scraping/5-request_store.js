#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

// Include request module
const request = require('request');

// Include fs module
const fs = require('fs');

// url/endpoint variable
const url = process.argv[2];

// Use request to fetch the data
request(url, function (err, response, body) {
  // Printing the error if occurred
  if (err) console.log(err);
  // writte to the given file
  fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
    if (err) console.log(error);
  });
});
