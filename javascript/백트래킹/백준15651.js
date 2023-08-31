let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");
let [n, m] = input[0].split(" ").map(Number);

let arr = Array.from({ length: n }, (_, i) => i + 1);

let result = [];
let selected = [];
function dfs(arr, depth) {
  if (depth === m) {
    result.push(selected.join(" "));
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    selected.push(arr[i]);
    dfs(arr, depth + 1);
    selected.pop();
  }
}

dfs(arr, 0);
console.log(result.join("\n"));
