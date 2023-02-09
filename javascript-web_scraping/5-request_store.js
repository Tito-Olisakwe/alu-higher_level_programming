#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, async function (err, res) {
  if (err) {
    console.log(err);
  } else {
    await fs.writeFile(filePath, res.body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
