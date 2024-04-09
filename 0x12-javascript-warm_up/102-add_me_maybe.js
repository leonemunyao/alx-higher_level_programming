#!/usr/bin/node
/*
A function that increments and calls a function. The function must be visible from outside. No var allowed.
prototype: function (number, theFunction)
*/
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
}

