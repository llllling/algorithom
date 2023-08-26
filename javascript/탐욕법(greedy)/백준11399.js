let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let N = Number(input[0]);
let arr = input[1].split(" ").map((x) => Number(x));
arr.sort((a, b) => a - b);

const arr2 = arr.reduce(
  (acc, cur) => {
    acc.summary += cur;
    acc.answer += acc.summary;
    return acc;
  },
  { answer: 0, summary: 0 }
);
console.log(arr2.answer);
