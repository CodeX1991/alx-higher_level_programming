#!/usr/bin/node
// A script that writes a string to a file

// Include fs module
const fs = require('fs');

// Use fs.writeFile() method to write to a file
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
  // Check status
  if (err) {
    console.log(err);
  }
});
