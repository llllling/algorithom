let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let n = Number(input[0]);
let arr = [];
let i = 1;
while (i <= n) {
  arr.push(input[i++].split(" ").map(Number));
}
arr.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  }
  return a[1] - b[1];
});
let count = 1;
let tmp = arr[0][1];
for (let i = 1; i < arr.length; i++) {
  if (tmp <= arr[i][0]) {
    count++;
    tmp = arr[i][1];
  }
}
console.log(count);
