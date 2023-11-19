#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  let i = 0;
  while (list[i]) {
    if (list[i] === searchElement) {
      occur++;
    }
    i++;
  }
  return (occur);
};
