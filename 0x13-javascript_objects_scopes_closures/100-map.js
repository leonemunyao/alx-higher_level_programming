#!/usr/bin/node

const { list } = require('./100-data');

/* A script that imports an array and computes a new array */

const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
