#!/usr/bin/node

const argCount = process.argv.length;

if (argCount === 2 || !(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
