#!/usr/bin/node

const arr = 'C is fun';
let i = parseInt(process.argv[2]);

if (!(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log(arr);
    i--;
  }
}
