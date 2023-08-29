let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs
  .readFileSync(__dirname + "/input.txt")
  .toString()
  .split("\n");

function palindrome(x) {
  return x == x.split("").reverse().join("");
}

let T = Number(input[0]);

for (let i = 1; i <= T; i++) {
  let str = input[i].slice(0, -1);
  if (palindrome(str)) {
    console.log(0);
    continue;
  }

  let flag = false;
  for (let j = 0; j < parseInt(str.length / 2); j++) {
    if (str[j] !== str[str.length - j - 1]) {
      // 대칭이 맞지 않을 경우

      //앞쪽 알파벳을 지워보고 대칭 검사 다시
      if (palindrome(str.slice(0, j) + str.slice(j + 1, str.length))) {
        flag = true;
      }
      // 뒤쪽 알파벳을 지워보고 대칭 검사 다시
      if (
        palindrome(
          str.slice(0, str.length - j - 1) +
            str.slice(str.length - j, str.length)
        )
      ) {
        flag = true;
      }
      break;
    }
  }
  if (flag) console.log(1);
  else console.log(2);
}
