#!/usr/bin/node

const argC = process.argv.length;

if (argC === 2) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (argC === 3) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
