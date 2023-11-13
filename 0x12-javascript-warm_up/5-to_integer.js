#!/usr/bin/node
const { argv } = require("process");
const arg = parseInt(argv[2], 10);
if (!isNaN(arg)) console.log(arg);
else console.log("Not a number");
