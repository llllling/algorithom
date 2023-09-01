let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number);
let graph = Array.from({ length: n + 1 }, () => []);

function dfs(x, dist) {
  if (visited[x]) return;
  visited[x] = true;
  distance[x] = dist;
  for (let [y, cost] of graph[x]) {
    dfs(y, dist + cost);
  }
}

for (let i = 1; i < n; i++) {
  let [a, b, c] = input[i].split(" ").map(Number);
  graph[a].push([b, c]);
  graph[b].push([a, c]);
}

for (let i = n; i < n + m; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  visited = Array.from({ length: n + 1 }, () => false);
  distance = Array.from({ length: n + 1 }, () => -1);
  dfs(x, 0);
  console.log(distance[y]);
}
