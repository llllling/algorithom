let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);
