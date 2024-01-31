#!/usr/bin/node

// this gets the content of a webpage and writes it into a file
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
const f = args[3];

request(url, (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(f, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
