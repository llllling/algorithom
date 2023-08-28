let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let pibo = [0, 1];
while (pibo[pibo.length - 1] < 1e9)
  pibo.push(pibo[pibo.length - 2] + pibo[pibo.length - 1]);

let idx = 1;
let T = Number(input[0]);
while (T > 0) {
  T--;
  let n = Number(input[idx++]);

  let result = [];
  let i = pibo.length - 1;
  while (n > 0) {
    // n이 0이 될 때까지
    if (n >= pibo[i]) {
      // 가능한 큰 피보나치 수부터 빼기
      n -= pibo[i];
      result.push(pibo[i]);
    }
    i--;
  }

  console.log(result.reverse().join(" "));
}
