#!/usr/bin/node

let count = 0; // Initialize a count variable to keep track of the number of arguments printed

exports.logMe = function (item) {
  console.log(count + ': ' + item); // Print the count and the current argument value
  count++; // Increment the count for the next call
};
