let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [k, n] = input[0].split(" ").map(Number);
let arr = input.slice(1).map(Number);

let start = 0;
let end = Math.max(...arr);
let result = 0;
while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let total = 0;
  for (x of arr) {
    total += Math.floor(x / mid);
  }
  if (total < n) {
    end = mid - 1;
  } else {
    start = mid + 1;
    result = mid;
  }
}

console.log(result);
