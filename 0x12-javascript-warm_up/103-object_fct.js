#!/usr/bin/node

/**
 Update this script by adding a new function incr that increments the integer value
 */

const myObject = {
  type: 'object',
  value: 12
};

function addIncr (obj) {
  obj.incr = function () {
    this.value++;
    console.log(this);
  };
}

console.log(myObject);
addIncr(myObject);
myObject.incr();
myObject.incr();
myObject.incr();
