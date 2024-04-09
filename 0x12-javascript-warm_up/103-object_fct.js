#!/usr/bin/node

/**
 Update this script by adding a new function incr that increments the integer value
 */
 const myObject = {
    type: 'object',
    value: 12,
    incr: function () {
        this.value++;
    }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

