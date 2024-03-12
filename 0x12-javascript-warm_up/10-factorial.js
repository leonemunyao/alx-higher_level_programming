#!/usr/bin/node

function factorial (i) {
  if (i < 0) {
    return (-1);
  }
  if (i === 0 || isNaN(i)) {
    return (1);
  }
  return (i * factorial(i - 1));
}

console.log(factorial(Number(process.argv[2])));
