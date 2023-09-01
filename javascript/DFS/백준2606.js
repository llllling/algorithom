let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let n = Number(input[0]);
let m = Number(input[1]);
let arr = Array.from({ length: n + 1 }, () => []);
for (let i = 2; i < m + 2; i++) {
  let [a, v] = input[i].split(" ").map(Number);
  arr[a].push(v);
  arr[v].push(a);
}

let visited = Array(n + 1).fill(false);
let cnt = 0;
function dfs(arr, v, visited) {
  visited[v] = true;
  cnt++;
  for (i of arr[v]) {
    if (!visited[i]) {
      dfs(arr, i, visited);
    }
  }
}

dfs(arr, 1, visited);
console.log(cnt - 1);
