#!/usr/bin/node

const len = process.argv.length;

if (len < 2 || !parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      if (j === parseInt(process.argv[2]) - 1) {
        console.log('X');
      } else {
        process.stdout.write('X');
      }
    }
  }
}
