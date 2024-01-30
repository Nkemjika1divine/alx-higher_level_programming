#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[3], (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
