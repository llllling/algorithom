//핵심 아이디어 : 해당 높이에 존재하는 화살이 없다면 화살을 새롭게 사용한다
let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let N = Number(input[0]);
let H = input[1].split(" ").map(Number);

let arrow = Array.from({ length: 1000001 }, () => 0);
let count = 0;
for (let i = 0; i < N; i++) {
  if (arrow[H[i]] === 0) {
    // 해당 높이에 화살이 없다면
    arrow[H[i] - 1]++;
    count++;
  } else {
    arrow[H[i]]--;
    arrow[H[i] - 1]++;
  }
}
console.log(count);
