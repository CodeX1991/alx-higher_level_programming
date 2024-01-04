#!/usr/bin/node
// A script that reads and prints the content of a file

// Include fs module
const fs = require('fs');

// Use fs.readFile() method to read the file
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  // Check status
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
