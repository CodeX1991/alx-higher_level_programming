#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      while (j < this.width) {
        if (j === this.width - 1) {
          console.log('x');
        } else {
          process.stdout.write('x');
        }
        j++;
      }
      i++;
    }
  }
};
