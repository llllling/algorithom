let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
let S = Number(input[0]);
let sum = 0;
let current = 0;
while (sum <= S) {
  current += 1;
  sum += current;
}

console.log(current - 1);
