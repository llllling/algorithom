let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

function isCycle(x, prev) {
  visited[x] = true;
  for (let y of graph[x]) {
    if (!visited[y]) {
      if (isCycle(y, x)) return true;
    } else if (y != prev) return true;
  }
  return false;
}

let line = 0;
let testCase = 1;
while (true) {
  let [n, m] = input[line++].split(" ").map(Number);
  if (n === 0 && m === 0) break;
  graph = Array.from({ length: n + 1 }, () => []);
  for (let i = line; i < line + m; i++) {
    let [a, b] = input[i].split(" ").map(Number);
    graph[a].push(b);
    graph[b].push(a);
  }

  let cnt = 0;
  visited = Array.from({ length: n + 1 }, () => false);
  for (let i = 1; i <= n; i++) {
    if (!visited[i]) {
      if (!isCycle(i, 0)) cnt++;
    }
  }

  if (cnt == 0) console.log(`Case ${testCase}: No trees.`);
  else if (cnt == 1) console.log(`Case ${testCase}: There is one tree.`);
  else console.log(`Case ${testCase}: A forest of ${cnt} trees.`);
  testCase++;
  line += m;
}
