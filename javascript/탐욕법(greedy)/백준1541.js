// 뺄셈(-) 연산자를 기준으로 최대한 많은 수를 묶는다
let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let text = input[0].split("-");
let result = 0;
for (let i = 0; i < text.length; i++) {
  let addArr = text[i].split("+");
  let addValue = addArr.reduce((acc, cur) => (acc += Number(cur)), 0);
  if (i === 0) {
    result = addValue;
  } else {
    result -= addValue;
  }
}
console.log(result);
