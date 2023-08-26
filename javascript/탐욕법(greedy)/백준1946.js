let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let T = Number(input[0]);
let c = 0;
let N = 0;
while (T > 0) {
  T--;

  let arr = [];
  N = Number(input[++c]);
  while (N > 0) {
    N--;
    arr.push(input[++c].split(" ").map(Number));
  }
  arr.sort((a, b) => a[0] - b[0]); //x순위 기준으로 오름차순 정렬
  let count = 0;
  let minValue = 100001;
  for (let [x, y] of arr) {
    if (y < minValue) {
      // y 순위 값이 가장 작다면 카운트
      minValue = y;
      count += 1;
    }
  }
  console.log(count);
}
