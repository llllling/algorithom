let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
let [n, m] = input[0].split(" ").map(Number);

let arr = Array.from({ length: n }, (_, i) => i + 1);
let selected = [];
let result = [];

function dfs(arr, depth, start) {
  if (depth === m) {
    result.push(selected.join(" "));
    return;
  }
  for (let i = start; i < arr.length; i++) {
    selected.push(arr[i]);
    dfs(arr, depth + 1, i); // 중복 조합이므로 i부터 시작
    selected.pop();
  }
}
dfs(arr, 0, 0);
console.log(result.join("\n"));
