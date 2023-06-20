export default function (a, b, c) {
  let res = ''
  if (a < 1 || a > 100 || b < 1 || b > 100 || c < 1 || c > 100) {
    res = '边超出范围'
  } else if (a + b > c && a + c > b && b + c > a) {
    if (a === b && b === c) {
      res = '等边三角形'
    } else if (a === b || b === c || a === c) {
      res = '等腰三角形'
    } else {
      res = '普通三角形'
    }
  } else {
    res = '无法构成三角形'
  }
  return res
}
