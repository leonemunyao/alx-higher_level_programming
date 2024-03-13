#!/usr/bin/node

exports.addMyNumber = function (number, theFunction) {
  theFunction(++number);
};
