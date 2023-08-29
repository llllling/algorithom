let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [l, w, h] = input[0].split(" ").map(Number);
let n = Number(input[1]);
let cube = Array(20).fill(0);
for (let i = 2; i < n + 2; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  cube[a] = b;
}

function nearestSquare(n) {
  let i = 0;
  while (Math.pow(2, i) <= n) {
    i++;
  }
  return i - 1;
}

let size = 19;
size = Math.min(nearestSquare(l), nearestSquare(w));
size = Math.min(size, nearestSquare(h));

let res = 0;
let used = 0;

for (let i = size; i >= 0; i--) {
  used *= 8; // i가 줄어들 수록 필요한 큐브의 개수는 8배 증가, requried에서 빼줄 때 해당 i의 기준을 큐브갯수를 빼줘야하므로
  cur = Math.pow(2, i);
  let requried =
    Math.floor(l / cur) * Math.floor(w / cur) * Math.floor(h / cur);

  let usage = Math.min(requried - used, cube[i]);
  used += usage;
  res += usage;
}

if (used == l * w * h) console.log(res); //박스 가득 채운 경우
else console.log(-1);
