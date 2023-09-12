#!/usr/bin/node

const BaseSquare = require('./5-square'); // Import the previous Square class

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // Default character is X
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
