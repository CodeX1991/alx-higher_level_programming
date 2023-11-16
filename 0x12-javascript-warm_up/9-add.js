#!/usr/bin/node

const len = process.argv.length;

if (len < 2) {
  console.log('NaN');
} else {
  function add (a, b) {
    console.log(a + b);
  }
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
