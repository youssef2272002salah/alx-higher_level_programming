#!/usr/bin/node

const { argv } = require('process');
const url = argv[2];

const request = require('request');
const options = {
  url,
  method: 'GET'
};
request(options, function (res) {
  console.log('code: ', res.statusCode);
});
