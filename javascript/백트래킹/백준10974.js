let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let n = Number(input[0]);

let arr = Array.from({ length: n }, (_, i) => i + 1);
let result = [];
let selected = [];
let visited = Array(n).fill(false);

function dfs(arr, depth) {
  if (depth === n) {
    result.push(selected.join(" "));
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    if (visited[i]) continue;
    selected.push(arr[i]);
    visited[i] = true;
    dfs(arr, depth + 1);
    selected.pop();
    visited[i] = false;
  }
}

dfs(arr, 0);
console.log(result.join("\n"));
