#!/usr/bin/node

if (process.argv.length <= 2) { console.log('Missing number of occurrences'); } else if (!isNaN(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) { console.log('C is fun'); }
}
