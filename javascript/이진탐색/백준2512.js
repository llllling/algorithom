let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);
let m = Number(input[2]);

let start = 1;
let end = Math.max(...arr);

let result = 0;
while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let total = 0;

  for (x of arr) {
    x > mid ? (total += mid) : (total += x);
  }
  if (total <= m) {
    result = mid;
    start = mid + 1;
  } else {
    end = mid - 1;
  }
}

console.log(result);
