#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

const data = process.argv[3];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.log(err);
  } else {
    fs.readFileSync(filePath, 'utf8');
  }
});
