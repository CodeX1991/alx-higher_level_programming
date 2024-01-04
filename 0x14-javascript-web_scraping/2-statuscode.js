#!/usr/bin/node
// A script that display the status code of a GET request

// Include request module
const request = require('request');

// Use request to fetch the data
request(process.argv[2], function (err, response) {
  // Printing the error if occurred
  if (err) {
    console.log(err);
  } else {
    // Printing status code
    console.log('code:', response.statusCode);
  }
});
