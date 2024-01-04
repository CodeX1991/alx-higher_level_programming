#!/usr/bin/node
// A script that computes the number of tass completed by user id

// Include request module
const request = require('request');

// url/endpoint variable
const url = process.argv[2];

// Use request to fetch the data
request(url, function (err, response, body) {
  // Handle error
  if (err) console.log(err);
  // Printing th number of movies
  const completedTasksByUsers = {};
  body = JSON.parse(body);

  for (let i = 0; i < body.length; i++) {
    const userId = body[i].userId;
    const completed = body[i].completed;

    if (completed && !completedTasksByUsers[userId]) {
      completedTasksByUsers[userId] = 0;
    }
    if (completed) ++completedTasksByUsers[userId];
  }
  console.log(completedTasksByUsers);
});
