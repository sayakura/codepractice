var path = require("path");
var util = require("util");

console.log(path.basename(__filename));

util.log(__dirname);
var path2 = path.join(__dirname, "public","file");
util.log(path2);
