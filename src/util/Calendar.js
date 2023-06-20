import moment from 'moment';

export default function Calendar(y, m, d) {
  if (y === null || m === null || d == null) {
    return '请输入合法参数'
  }
  if (y < 1900 || y > 2100) {
    return '年份超出范围'
  }
  if (m > 12 || m < 1) {
    return '输入日期不存在'
  }
  if (m === 4 || m === 6 || m === 9 || m === 11) {
    if (d > 30 || d < 1) {
      return '输入日期不存在'
    }
  } else if (m === 2) {
    if ((y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0)) {
      if (d > 29 || d < 1) {
        return '输入日期不存在'
      }
    } else {
      if (d > 28 || d < 1) {
        return '输入日期不存在'
      }
    }
  } else {
    if (d > 31 || d < 1) {
      return '输入日期不存在'
    }
  }
  var newDate = moment()
  newDate.set('year', y)
  newDate.set('month', m - 1)
  newDate.set('date', d)
  newDate.startOf('day')

  newDate.add(1, 'days')

  return newDate.format('YYYY-MM-DD')
}
