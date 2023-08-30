let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number); // 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
let arr = Array.from({ length: n }, (_, i) => i + 1); // 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

let result = [];
let selected = []; // 선택된 수열을 담는 배열
let visited = Array(n).fill(false); // 방문 여부를 체크하는 배열
function dfs(arr, depth) {
  if (depth === m) {
    result.push(selected.join(" "));
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    if (visited[i]) continue;
    selected.push(arr[i]);
    visited[i] = true;
    dfs(arr, depth + 1);
    visited[i] = false;
    selected.pop();
  }
}

dfs(arr, 0);
console.log(result.join("\n"));
