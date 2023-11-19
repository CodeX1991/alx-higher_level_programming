#!/usr/bin/node

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      let i = 0;
      while (i < this.size) {
        let j = 0;
        while (j < this.size) {
          if (j === this.size - 1) {
            console.log(c);
          } else {
            process.stdout.write(c);
          }
          j++;
        }
        i++;
      }
    } else {
      super.print(c);
    }
  }
};
