#!/usr/bin/node

// computes the number of tasks completed by user id
const request = require('request');
// const fs = require('fs');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    for (const character of JSON.parse(body).characters) {
      request(character, (err, code, body) => {
        if (err) {
          console.error(err);
        } else {
  i        console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
