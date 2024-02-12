#!/usr/bin/node

function fact (num) {
  return (num * (num - 1));
}

if (process.argv.length <= 2) { console.log(1); } else { console.log(fact(parseInt(process.argv[2]))); }
