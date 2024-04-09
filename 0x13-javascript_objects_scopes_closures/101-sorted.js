#!/usr/bin/node
const { dict } = require('./101-data');

/* A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence */
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
console.log(newDict);
