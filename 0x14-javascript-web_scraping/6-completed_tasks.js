#!/usr/bin/node

// computes the number of tasks completed by user id
const request = require('request');
// const fs = require('fs');
const args = process.argv;
const url = args[2];
// const f = args[3];

request(url, (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    const users = {};
    for (const user in JSON.parse(body)) {
      if (JSON.parse(body)[user].completed) {
        users[JSON.parse(body)[user].userId] = (users[JSON.parse(body)[user].userId] || 0) + 1;
      }
    }
    console.log(users);
  }
});
