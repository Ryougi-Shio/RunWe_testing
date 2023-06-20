<template>
  <div>
    <b-jumbotron style="height: 80px" header="电信收费问题" class="title">
  </b-jumbotron>
  <div STYLE="display:flex">
      <el-card style="width:45%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">验证部分</span>
      <el-button style="font-size:20px;font-weight:bold;float: right; padding: 3px 0" @click="calculate(callTime,count)" type="text">进行测试</el-button>
    </div>
    <div>
      <b-input-group>
        <b-input-group-prepend is-text>通话时间: </b-input-group-prepend>
        <b-form-input v-model="callTime" type="number" placeholder="请输入通话时间"></b-form-input>
      </b-input-group>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div>
      <b-input-group>
        <b-input-group-prepend is-text>未按时缴费次数: </b-input-group-prepend>
        <b-form-input v-model="count" type="number" placeholder="请输入未按时缴费次数"></b-form-input>
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
    <div style="display:flex">
      <b-button style="margin-left: 2vw"  @click="changeTable(1)" variant="dark">边界值法</b-button>
      <b-dropdown style="margin-left: 30px" text="等价类" variant="dark"  @click="handleClick">
        <b-dropdown-item :id="2" @click="changeTable(2)" >强一般等价类</b-dropdown-item>
        <b-dropdown-item  :id="3" @click="changeTable(3)">强健壮等价类</b-dropdown-item>
      </b-dropdown>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div class="input-separator"></div>
    <div>
      <b-button style="margin-left: 2vw"  :id="4" @click="changeTable(4)" variant="dark">决策表法</b-button>
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
        prop="minute"
        label="minute"
        width="300">
      </el-table-column>
      <el-table-column
        prop="count"
        label="count"
        width="300">
      </el-table-column>
      <el-table-column
        prop="discount"
        label="discount"
        width="300">
      </el-table-column>
      <el-table-column
        prop="output"
        label="ouput"
        width="400">
      </el-table-column>
    </el-table>
  </el-card>
  </div>
  </div>
</template>

<script>
/* eslint-disable*/

export default {
  name: 'DianXinFeiYong',
  data() {
    return {
      radio: '1',
      BASIC_FARE: 25,
      PER_MINUTE_FARE: 0.15,
      MINUTE_MAX: 44640,
      COUNT_MAX: 11,
      callTime: 0.0,
      count: 0,
      result:"",
      targetTable:[],
      items: [],
      items2: [],
      items3: [],
      items4: [],
    }
  },
  methods: {
    calculate(minute, count) {
      this.result=""
      if (minute < 0 || count < 0 || minute > this.MINUTE_MAX || count > this.COUNT_MAX) {
        this.result="输入的时间或次数超出范围，不满足条件";
        return "输入的时间或次数超出范围，不满足条件"
      }
      let money = this.BASIC_FARE;
      if (minute <= 60) {
        if (count < 1) {
          money += minute * this.PER_MINUTE_FARE * (1 - 0.01)
        } else {
          money += minute * this.PER_MINUTE_FARE;
        }
      }else if(minute<=120){
        if (count < 2) {
          money += minute * this.PER_MINUTE_FARE * (1 - 0.015)
        } else {
          money += minute * this.PER_MINUTE_FARE;
        }
      }else if(minute<=180){
        if (count < 3) {
          money += minute * this.PER_MINUTE_FARE * (1 - 0.02)
        } else {
          money += minute * this.PER_MINUTE_FARE;
        }
      }else if(minute<=300){
        if (count < 3) {
          money += minute * this.PER_MINUTE_FARE * (1 - 0.025)
        } else {
          money += minute * this.PER_MINUTE_FARE;
        }
      }else {
        if (count < 6) {
          money += minute * this.PER_MINUTE_FARE * (1 - 0.03)
        } else {
          money += minute * this.PER_MINUTE_FARE;
        }
      }
      this.result=money;
      return money;
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
    let result =
      '| 1    | 1      | 0     | 1.0%               | 25.148500        |\n' +
      '| 2    | 2      | 1     | 1.0%               | 25.297000        |\n' +
      '| 3    | 4      | 1     | 1.0%               | 25.594000        |\n' +
      '| 4    | 6      | 0     | 1.0%               | 25.891000        |\n' +
      '| 5    | 30     | 0     | 1.0%               | 29.432500        |\n' +
      '| 6    | 59     | 1     | 1.0%               | 33.717250        |\n' +
      '| 7    | 60     | 2     | 1.0%               | 33.865000        |\n' +
      '| 8    | 61     | 0     | 1.5%               | 34.012750        |\n' +
      '| 9    | 64     | 1     | 1.5%               | 34.456000        |\n' +
      '| 10   | 90     | 0     | 1.5%               | 38.297500        |\n' +
      '| 11   | 118    | 1     | 1.5%               | 42.434500        |\n' +
      '| 12   | 119    | 3     | 1.5%               | 42.582250        |\n' +
      '| 13   | 120    | 0     | 1.5%               | 42.730000        |\n' +
      '| 14   | 121    | 3     | 2.0%               | 42.787000        |\n' +
      '| 15   | 129    | 2     | 2.0%               | 43.963000        |\n' +
      '| 16   | 150    | 3     | 2.0%               | 47.050000        |\n' +
      '| 17   | 178    | 2     | 2.0%               | 51.166000        |\n' +
      '| 18   | 179    | 0     | 2.0%               | 51.313000        |\n' +
      '| 19   | 180    | 3     | 2.0%               | 51.460000        |\n' +
      '| 20   | 181    | 3     | 2.5%               | 51.471250        |\n' +
      '| 21   | 184    | 2     | 2.5%               | 51.910000        |\n' +
      '| 22   | 240    | 1     | 2.5%               | 60.100000        |\n' +
      '| 23   | 274    | 2     | 2.5%               | 65.072500        |\n' +
      '| 24   | 297    | 0     | 2.5%               | 68.436250        |\n' +
      '| 25   | 299    | 6     | 2.5%               | 68.728750        |\n' +
      '| 26   | 300    | 6     | 2.5%               | 68.875000        |\n' +
      '| 27   | 301    | 6     | 3.0%               | 68.795500        |\n' +
      '| 28   | 304    | 1     | 3.0%               | 69.232000        |\n' +
      '| 29   | 379    | 2     | 3.0%               | 80.144500        |\n' +
      '| 30   | 451    | 3     | 3.0%               | 90.620500        |\n' +
      '| 31   | 503    | 20    | 3.0%               | 98.186500        |\n' +
      '| 32   | 19304  | 5     | 3.0%               | 2833.732000      |\n' +
      '| 33   | 29487  | 2     | 3.0%               | 4315.358500      |\n' +
      '| 34   | 43924  | 4     | 3.0%               | 6415.942000      |\n' +
      '| 35   | 44630  | 2     | 3.0%               | 6518.665000      |\n' +
      '| 36   | 44638  | 6     | 3.0%               | 6519.829000      |\n' +
      '| 37   | 44639  | 0     | 3.0%               | 6519.974500      |\n' +
      '| 38   | 44640  | 6     | 3.0%               | 6520.120000      |\n' +
      '| 39   | -1     | 0     | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 40   | 0      | 2     | 0%                 | 25                            |\n' +
      '| 41   | 54250  | 1     | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 42   | 234    | -1    | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 43   | 132    | -4    | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 44   | 521    | 15    | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 45   | 213    | 42    | 0%                 | 输入的时间或次数超出范围，不满足条件 |' +
      '| 46   | -1     | -1    | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 47   | -4     | -12   | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 48   | 54250  | -2    | 0%                 | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 49   | 678934 | 54    | 0%                 | 输入的时间或次数超出范围，不满足条件 |'
    let resarray = result.split('\n')
    for (var single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items.push({
        序号: temp[1],
        minute: temp[2],
        count: temp[3],
        discount: temp[4],
        output: temp[5],
      })
    }
    result =
      '| 1    | 12     | 1     | 1%                 | 26.782           |\n' +
      '| 2    | 20     | 2     | 0                  | 28               |\n' +
      '| 3    | 30     | 3     | 0                  | 29.5             |\n' +
      '| 4    | 40     | 5     | 0                  | 31               |\n' +
      '| 5    | 53     | 8     | 0                  | 32.95            |\n' +
      '| 6    | 63     | 1     | 1.50%              | 34.30825         |\n' +
      '| 7    | 70     | 2     | 1.50%              | 35.3425          |\n' +
      '| 8    | 83     | 3     | 0                  | 37.45            |\n' +
      '| 9    | 95     | 6     | 0                  | 39.25            |\n' +
      '| 10   | 118    | 9     | 0                  | 42.7             |\n' +
      '| 11   | 128    | 1     | 2%                 | 43.816           |\n' +
      '| 12   | 146    | 2     | 2%                 | 46.462           |\n' +
      '| 13   | 156    | 3     | 2%                 | 47.932           |\n' +
      '| 14   | 167    | 4     | 0%                 | 50.05            |\n' +
      '| 15   | 176    | 7     | 0%                 | 51.4             |\n' +
      '| 16   | 207    | 1     | 2.50%              | 55.27375         |\n' +
      '| 17   | 213    | 2     | 2.50%              | 56.15125         |\n' +
      '| 18   | 246    | 3     | 2.50%              | 60.9775          |\n' +
      '| 19   | 257    | 5     | 0.00%              | 63.55            |\n' +
      '| 20   | 269    | 10    | 0.00%              | 65.35            |\n' +
      '| 21   | 345    | 1     | 3%                 | 75.1975          |\n' +
      '| 22   | 364    | 2     | 3%                 | 77.962           |\n' +
      '| 23   | 465    | 3     | 3%                 | 92.6575          |\n' +
      '| 24   | 3567   | 5     | 3%                 | 543.9985         |\n' +
      '| 25   | 4567   | 8     | 0%                 | 710.05           |'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items2.push({
        序号: temp[1],
        minute: temp[2],
        count: temp[3],
        discount: temp[4],
        output: temp[5],
      })
    }
    result =
      '| 1    | -2     | 1     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 2    | 0      | 2     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 3    | -4     | 3     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 4    | -15    | 5     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 5    | -20    | 8     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 6    | 100000 | 1     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 7    | 50000  | 2     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 8    | 64765  | 3     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 9    | 74253  | 4     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 10   | 83432  | 9     | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 11   | 24     | -2    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 12   | 64     | -4    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 13   | 134    | -6    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 14   | 294    | -20   | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 15   | 355    | -30   | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 16   | 32     | 12    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 17   | 83     | 34    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 18   | 156    | 45    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 19   | 233    | 76    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 20   | 546    | 666   | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 21   | -2     | -5    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 22   | -1     | 53    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 23   | 98783  | -8    | 0                  | 输入的时间或次数超出范围，不满足条件 |\n' +
      '| 24   | 183748 | 15    | 0                  | 输入的时间或次数超出范围，不满足条件 |'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items3.push({
        序号: temp[1],
        minute: temp[2],
        count: temp[3],
        discount: temp[4],
        output: temp[5],
      })
    }
    result =
      '| 1    | 20     | 0     | 1.00%              | 27.97            |\n' +
      '| 2    | 45     | 2     | 0.00%              | 31.75            |\n' +
      '| 3    | 102    | 1     | 1.50%              | 40.0705          |\n' +
      '| 4    | 113    | 3     | 0.00%              | 41.95            |\n' +
      '| 5    | 156    | 2     | 2.00%              | 47.932           |\n' +
      '| 6    | 164    | 4     | 0.00%              | 49.6             |\n' +
      '| 7    | 213    | 2     | 2.50%              | 56.15125         |\n' +
      '| 8    | 254    | 5     | 0.00%              | 63.1             |\n' +
      '| 9    | 358    | 6     | 3.00%              | 77.089           |\n' +
      '| 10   | 546    | 9     | 0.00%              | 106.9            |'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items4.push({
        序号: temp[1],
        minute: temp[2],
        count: temp[3],
        discount: temp[4],
        output: temp[5],
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
.text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
