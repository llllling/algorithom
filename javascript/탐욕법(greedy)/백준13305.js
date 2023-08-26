let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let N = Number(input[0]);
let dist = input[1].split(" ").map(Number);
let cost = input[2].split(" ").map(Number);

// 4 => 2로 변경한 이유는 자기보다 뒤에 있는 비싼 주유소에 대해서 미리 결제하는 것으로 이해
// [5, 2, 4, 1] -> [5, 2, 2, 1]
let minCost = cost[0];
for (let i = 0; i < N; i++) {
  minCost = Math.min(minCost, cost[i]);
  cost[i] = minCost;
}
// 도로당 이동 비용의 합 계산
let answer = BigInt(0);
for (let i = 0; i < N - 1; i++) {
  // JavaScript에서 큰 정수를 처리할 때는 BigInt 사용
  answer += BigInt(dist[i]) * BigInt(cost[i]);
}
console.log(String(answer)); // 뒤에 붙는 'n' 제거
