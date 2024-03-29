let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = input[1].split(" ").map(Number);

let start = 0;
let end = Math.max(...arr);

let result = 0;
while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let total = 0;
  for (x of arr) {
    total += Math.max(x - mid, 0);
  }
  if (total >= m) {
    // 나무의 양이 충분한 경우 덜 자르기(높이 키우기)
    result = mid;
    start = mid + 1;
  } else {
    // 나무의 양이 부족한 경우 더 많이 자르기(높이 줄이기)
    end = mid - 1;
  }
}

console.log(result);
