// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
let n = Number(input[0]);
let arr = [];

for (let i = 1; i <= n; i++) {
  let [age, name] = input[i].split(" ");
  arr.push([Number(age), name]);
}

arr.sort((a, b) => a[0] - b[0]);

let answer = "";
for (let x of arr) answer += x[0] + " " + x[1] + "\n";
console.log(answer);
