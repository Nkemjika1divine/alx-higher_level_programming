#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (err, code, reponse) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(reponse).title);
  }
});
