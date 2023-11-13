#!/usr/bin/node
const { argv } = require('process');
const a = parseInt(argv[2], 10);

function factorial (num) {
  if (num <= 1) return 1;
  return num * factorial(num - 1);
}

if (isNaN(a)) console.log(1);
else console.log(factorial(a));
