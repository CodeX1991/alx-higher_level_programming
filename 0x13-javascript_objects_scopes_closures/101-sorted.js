#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

Object.keys(dict).map((key) => {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});
console.log(newDict);
