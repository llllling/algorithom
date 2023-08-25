let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let arr = input[0].split("").map((x) => Number(x));
arr.sort((a, b) => b - a);
console.log(arr.join(""));
