#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <outputFile>');
  process.exit(1);
}

const file1 = args[0];
const file2 = args[1];
const outputFile = args[2];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1}: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2}: ${err.message}`);
      process.exit(1);
    }

    const concatenatedData = `${data1}${data2}`;

    fs.writeFile(outputFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing ${outputFile}: ${err.message}`);
        process.exit(1);
      }
      console.log(`Concatenated data has been written to ${outputFile}`);
    });
  });
});
