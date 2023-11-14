#!/usr/bin/node

const OriginalSquare = require('./5-square');

class Square extends OriginalSquare {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        console.log(c);
      }
    }
  }
}

module.exports = Square;
