#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 2) {
    return 0;
  }

  let firstMax = Number.MIN_SAFE_INTEGER;
  let secondMax = Number.MIN_SAFE_INTEGER;

  for (const arg of arr) {
    const num = parseInt(arg);
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num < firstMax) {
      secondMax = num;
    }
  }

  return secondMax;
}

const args = process.argv.slice(2);
const result = secondBiggest(args);

console.log(result);
