<template>
    <div>
    <b-jumbotron style="height: 80px" header="万年历问题" class="title">
  </b-jumbotron>
  <div STYLE="display:flex">
      <el-card style="width:45%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">验证部分</span>
      <el-button style="font-size:20px;font-weight:bold;float: right; padding: 3px 0" @click="onSubmit" type="text">进行测试</el-button>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>年: </b-input-group-prepend>
      <b-form-input v-model.number="a" type="number" placeholder="请输入年份(1900~2100)"></b-form-input>
    </b-input-group>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>月: </b-input-group-prepend>
      <b-form-input v-model.number="b" type="number" placeholder="请输入月份(1~12)"></b-form-input>
    </b-input-group>
    </div>
    <div class="input-separator"></div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>日: </b-input-group-prepend>
      <b-form-input v-model.number="c" type="number" placeholder="请输入日期"></b-form-input>
    </b-input-group>
    </div>
    <div class="input-separator"></div>
    <div>
      <p style="font-size:20px;font-weight:bold;">结果:{{ result }}</p>
    </div>
  </el-card>
  <el-card style="margin-left:20px;width:50%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">装载用例</span>
    </div>
    <div>
      <b-dropdown style="margin-left: 2vw" text="边界值" variant="dark"  @click="handleClick">
      <b-dropdown-item @click="changeTable(1)">基本边界值</b-dropdown-item>
      <b-dropdown-item @click="changeTable(2)">健壮性边界值</b-dropdown-item>
    </b-dropdown>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <b-dropdown style="margin-left: 2vw" text="等价类" variant="dark"  @click="handleClick">
      <b-dropdown-item @click="changeTable(4)">有效等价类</b-dropdown-item>
      <b-dropdown-item @click="changeTable(5)">无效等价类</b-dropdown-item>
    </b-dropdown>
    <div class="input-separator"></div>
    <div>
      <b-button style="margin-left: 2vw" @click="changeTable(3)" variant="dark">决策表法</b-button>
    </div>
    <div class="input-separator"></div>
  </el-card>
  </div>
  <div>
    <el-card style="margin-top:30px;width:95%;height:800px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">执行用例</span>
    </div>
    <el-table
      :data="targetTable"
      height="800"
      border
      stripe
      style="width: 100%">
      <el-table-column
        prop="序号"
        label="序号"
        width="300">
      </el-table-column>
      <el-table-column
        prop="年"
        label="年"
        width="300">
      </el-table-column>
      <el-table-column
        prop="月"
        label="月"
        width="300">
      </el-table-column>
      <el-table-column
        prop="日"
        label="日"
        width="300">
      </el-table-column>
      <el-table-column
        prop="下一天"
        label="下一天"
        width="400">
      </el-table-column>
    </el-table>
  </el-card>
  </div>
  </div>
</template>

<script>
import Calendar from '@/util/Calendar'

/* eslint-disable*/
export default {
  name: 'WanNianLi',
  data() {
    return {
      items: [],
      items2: [],
      items3: [],
      items4: [],
      items5: [],
      targetTable: [],
      result: ""
    }
  },
  methods: {
    onSubmit() {
      this.result = Calendar(this.a, this.b, this.c)
    },
    changeTable(id){
      if(id==1)
      {
        this.targetTable=this.items;
        console.log("success");
      }
      else if(id==2)
      {
        this.targetTable=this.items2;
      }
      else if(id==3)
      {
        this.targetTable=this.items3;
      }
      else if(id==4)
      {
        this.targetTable=this.items4;
      }
      else if(id==5)
      {
        this.targetTable=this.items5;
      }
    }
  },
  mounted() {
    let result = '1    | 1900    | 6       | 15      | 1900.6.16      \n' +
      ' 2    | 1901    | 6       | 15      | 1901.6.16      \n' +
      ' 3    | 2000    | 6       | 15      | 2000.6.16      \n' +
      ' 4    | 2099    | 6       | 15      | 2099.6.16      \n' +
      ' 5    | 2100    | 6       | 15      | 2100.6.16      \n' +
      ' 6    | 2000    | 1       | 15      | 2000.1.16      \n' +
      ' 7    | 2000    | 2       | 15      | 2000.2.16      \n' +
      ' 8    | 2000    | 11      | 15      | 2000.11.16     \n' +
      ' 9    | 2000    | 12      | 15      | 2000.12.16     \n' +
      ' 10   | 2000    | 6       | 1       | 2000.6.2       \n' +
      ' 11   | 2000    | 6       | 2       | 2000.6.3       \n' +
      ' 12   | 2000    | 6       | 15      | 2000.6.16      \n' +
      ' 13   | 2000    | 6       | 27      | 2000.6.28      \n' +
      ' 14   | 2000    | 6       | 28      | 2000.6.29      \n' +
      ' 15   | 2000    | 6       | 29      | 2000.6.30      \n' +
      ' 16   | 2000    | 6       | 30      | 2000.7.1       \n' +
      ' 17   | 2000    | 6       | 31      | 输入日期不存在  \n' +
      '18   | 1999    | 2       | 28      | 1999.3.1       \n' +
      ' 19   | 1999    | 2       | 29      | 输入日期不存在 \n' +
      ' 20   | 1999    | 2       | 30      | 输入日期不存在 \n' +
      ' 21   | 1999    | 2       | 31      | 输入日期不存在 \n' +
      ' 22   | 2000    | 2       | 28      | 2000.2.29      \n' +
      ' 23   | 2000    | 2       | 29      | 2000.3.1       \n' +
      ' 24   | 2000    | 2       | 30      | 输入日期不存在 \n' +
      ' 25   | 2000    | 2       | 31      | 输入日期不存在 \n' +
      ' 26   | 2000    | 7       | 30      | 2000.7.31      \n' +
      ' 27   | 2000    | 7       | 31      | 2000.8.1       \n' +
      ' 28   | 2000    | 12      | 30      | 2000.12.31     \n' +
      ' 29   | 2000    | 12      | 31      | 2001.1.1     '
    let resarray = result.split('\n')
    for (var single in resarray) {
      let temp = resarray[single].split('|')
      // console.log(temp)
      this.items.push({
        序号: temp[0],
        年: temp[1],
        月: temp[2],
        日: temp[3],
        下一天: temp[4],
      })
    }
    result = '1    | 1900    | 6       | 15      | 1900.6.16      \n' +
      ' 2    | 1901    | 6       | 15      | 1901.6.16      \n' +
      ' 3    | 2000    | 6       | 15      | 2000.6.16      \n' +
      ' 4    | 2099    | 6       | 15      | 2099.6.16      \n' +
      ' 5    | 2100    | 6       | 15      | 2100.6.16      \n' +
      ' 6    | 2000    | 1       | 15      | 2000.1.16      \n' +
      ' 7    | 2000    | 2       | 15      | 2000.2.16      \n' +
      ' 8    | 2000    | 11      | 15      | 2000.11.16     \n' +
      ' 9    | 2000    | 12      | 15      | 2000.12.16     \n' +
      ' 10   | 2000    | 6       | 1       | 2000.6.2       \n' +
      ' 11   | 2000    | 6       | 2       | 2000.6.3       \n' +
      ' 12   | 2000    | 6       | 15      | 2000.6.16      \n' +
      ' 13   | 2000    | 6       | 27      | 2000.6.28      \n' +
      ' 14   | 2000    | 6       | 28      | 2000.6.29      \n' +
      ' 15   | 2000    | 6       | 29      | 2000.6.30      \n' +
      ' 16   | 2000    | 6       | 30      | 2000.7.1       \n' +
      ' 17   | 2000    | 6       | 31      | 输入日期不存在 \n' +
      '18   | 1999    | 2       | 28      | 1999.3.1       \n' +
      ' 19   | 1999    | 2       | 29      | 输入日期不存在 \n' +
      ' 20   | 1999    | 2       | 30      | 输入日期不存在 \n' +
      ' 21   | 1999    | 2       | 31      | 输入日期不存在 \n' +
      ' 22   | 2000    | 2       | 28      | 2000.2.29      \n' +
      ' 23   | 2000    | 2       | 29      | 2000.3.1       \n' +
      ' 24   | 2000    | 2       | 30      | 输入日期不存在 \n' +
      ' 25   | 2000    | 2       | 31      | 输入日期不存在 \n' +
      ' 26   | 2000    | 7       | 30      | 2000.7.31      \n' +
      ' 27   | 2000    | 7       | 31      | 2000.8.1       \n' +
      ' 28   | 2000    | 12      | 30      | 2000.12.31     \n' +
      ' 29   | 2000    | 12      | 31      | 2001.1.1     ' +
      '30    | 1899    | 6       | 15      | 年份超出范围   \n' +
      ' 31    | 2101    | 6       | 15      | 年份超出范围   \n' +
      ' 32    | 2000    | 0       | 15      | 输入日期不存在 \n' +
      ' 33    | 2000    | 13      | 15      | 输入日期不存在 \n' +
      ' 34    | 2000    | 6       | 0       | 输入日期不存在 \n' +
      ' 35    | 2000    | 6       | 32      | 输入日期不存在'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      // console.log(temp)
      this.items2.push({
        序号: temp[0],
        年: temp[1],
        月: temp[2],
        日: temp[3],
        下一天: temp[4],
      })
    }
    result = '| 1    | 2015 | 3     | 27   | day+1                 |\n' +
      '| 2    | 2016 | 12    | 16   | day+1                 |\n' +
      '| 3    | 2002 | 4     | 20   | day+1                 |\n' +
      '| 4    | 2012 | 2     | 28   | day+1                 |\n' +
      '| 5    | 2015 | 1     | 31   | day=1,month+1         |\n' +
      '| 6    | 2016 | 2     | 29   | day=1,month+1         |\n' +
      '| 7    | 2017 | 2     | 28   | day=1,month+1         |\n' +
      '| 8    | 2016 | 4     | 30   | day=1,month+1         |\n' +
      '| 9    | 2016 | 12    | 31   | day=1,month=1，year+1 |'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      // console.log(temp)
      this.items3.push({
        序号: temp[1],
        年: temp[2],
        月: temp[3],
        日: temp[4],
        下一天: temp[5],
      })
    }
    result = '| 1        | 2007,2,25 | 2007.2.26  |\n' +
      '   | 2        | 2008,2,28 | 2008.2.29 |\n' +
      '   | 3        | 2005,5,30 | 2005.5.31 |\n' +
      '   | 4        | 1990,4,18 | 1990.4.19 |'
    result = result.replaceAll('*', '')
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      this.items4.push({
        序号: temp[1],
        年: temp[2],
        下一天: temp[3],
      })
    }
    result = '| 1        | 1895,10,31 | 年份超出范围        |\n' +
      '   | 2        | 2150,2,1   | 年份超出范围        |\n' +
      '   | 3        | 2008,-1,1  | 输入日期不存在        |\n' +
      '   | 4        | 2008,13,1  | 输入日期不存在        |\n' +
      '   | 5        | 2008,1,-1  | 输入日期不存在        |\n' +
      '   | 6        | 2007,2,29  | 输入日期不存在       |\n' +
      '   | 7        | 2008,2,30  | 输入日期不存在       |\n' +
      '   | 8        | 2019,5,33  | 输入日期不存在       |\n' +
      '   | 9        | 2019,4,31  | 输入日期不存在       '
    result = result.replaceAll('*', '')
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      // console.log(temp)
      this.items5.push({
        序号: temp[1],
        年: temp[2],
        下一天: temp[3],
      })
    }
  }
}
</script>

<style scoped>
.title h1 {
  font-size: 36px;
}

.input-separator {
  height: 30px;
}
</style>
