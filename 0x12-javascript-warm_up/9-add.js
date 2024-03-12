#!/usr/bin/node

function add (i, j) {
  const k = i + j;
  console.log(k);
}

add(Number(process.argv[2]), Number(process.argv[3]));
