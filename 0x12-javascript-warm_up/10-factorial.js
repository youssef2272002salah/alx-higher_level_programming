#!/usr/bin/node

function fact (num) {
  if (num === 1) { return 1; } else { return (num * fact(num - 1)); }
}

if (process.argv.length <= 2) { console.log(1); } else { console.log(fact(parseInt(process.argv[2]))); }
