#!/usr/bin/node

const array1 = require('./100-data.js').list;

let index = 0;
const map1 = array1.map((num) => num * index++);

console.log(array1);
console.log(map1);
