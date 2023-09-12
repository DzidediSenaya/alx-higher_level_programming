#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h || w; // If h is not provided, use w as the default value.
  }
}

module.exports = Rectangle;
