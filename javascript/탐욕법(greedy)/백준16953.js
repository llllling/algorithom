let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

const [A, B] = input[0].split(" ").map(Number);
let result = 0;
let tmpB = B;
while (true) {
  if (tmpB === A) {
    result++;
    break;
  }

  if (tmpB % 2 === 0) {
    tmpB = tmpB / 2; //2로나누어떨어지는 경우
  } else if (tmpB % 10 === 1) {
    // 일의 자릿수가 1인 경우
    tmpB = parseInt(tmpB / 10);
  } else {
    result = -1;
    break;
  }
  result++;
}

console.log(result);
