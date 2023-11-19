#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let listCount = list.length - 1;
  let i = 0;
  while (list[i]) {
    newList[i] = list[listCount];
    i++;
    listCount--;
  }
  return (newList);
};
