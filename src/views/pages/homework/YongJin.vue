<template>
<div>
    <b-jumbotron style="height: 80px" header="电脑销售问题" class="title">
  </b-jumbotron>
  <div STYLE="display:flex">
      <el-card style="width:45%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">验证部分</span>
      <el-button style="font-size:20px;font-weight:bold;float: right; padding: 3px 0" @click="onSubmit" type="text">进行测试</el-button>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>主机销售数量: </b-input-group-prepend>
      <b-form-input
          id="input-live"
          v-model="a"
          :state="aState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="请输入主机销售数量"
          trim
        ></b-form-input>
        <b-form-invalid-feedback id="input-live-feedback">
          请输入1-70的整数
        </b-form-invalid-feedback>
    </b-input-group>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>显示器销售数量: </b-input-group-prepend>
      <b-form-input
          id="input-live2"
          v-model="b"
          :state="bState"
          aria-describedby="input-live2-help input-live-feedback"
          placeholder="请输入显示器销售数量"
          trim
        ></b-form-input>
        <b-form-invalid-feedback id="input-live-feedback">
          请输入1-80的整数
        </b-form-invalid-feedback>
    </b-input-group>
    </div>
    <div class="input-separator"></div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>外设销售数量: </b-input-group-prepend>
      <b-form-input
          id="input-live2"
          v-model="c"
          :state="cState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="请输入外设销售数量"
          trim
        ></b-form-input>
        <b-form-invalid-feedback id="input-live-feedback">
          请输入1-90的整数
        </b-form-invalid-feedback>
    </b-input-group>
    </div>
    <div class="input-separator"></div>
    <div>
      <p style="font-size:20px;font-weight:bold;">结果:{{ salary }}</p>
    </div>
  </el-card>
  <el-card style="margin-left:20px;width:50%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">装载用例</span>
    </div>
    <div>
      <b-button style="margin-left: 2vw" @click="changeTable(1)" variant="dark">考虑销售总额的边界</b-button>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <b-button style="margin-left: 2vw" @click="changeTable(2)" variant="dark">只考虑输入变量边界</b-button>
    <div class="input-separator"></div>
    <div>
      <b-button style="margin-left: 2vw" @click="changeTable(4)" variant="dark">考虑健壮性</b-button>
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
        prop="主机销量"
        label="主机销量"
        width="300">
      </el-table-column>
      <el-table-column
        prop="显示器销量"
        label="显示器销量"
        width="300">
      </el-table-column>
      <el-table-column
        prop="外设销量"
        label="外设销量"
        width="300">
      </el-table-column>
      <el-table-column
        prop="销售总额"
        label="销售总额"
        width="400">
      </el-table-column>
      <el-table-column
        prop="佣金"
        label="佣金"
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
  name: "YongJin",
  data() {
    return {
      a: '',
      b: '',
      c: '',
      aState:" ",
      bState:" ",
      cState:" ",
      sum: 0,
      salary: "",
      items:[],
      targetTable: [],
      items2:[],
      items3:[],
      items4:[],
      items5:[]
    };
  },

  computed:{
    // bState(){
    //   if(this.b < 1 || this.b>80 )return false;
    //     else return true;
    // },
    // cState(){
    //   if(this.c < 1 || this.c>90 )return false;
    //     else return true;
    // }
  },
  methods: {
    judgeInput(){
      var numReg = /^[0-9]*$/
      var numRe = new RegExp(numReg)
      if (!numRe.test(this.a)){
        this.aState = false;
      }else if(this.a < 1 || this.a>70){
        this.aState = false;
      }else this.aState = true;

      if (!numRe.test(this.b)){
        this.bState = false;
      }else if(this.b < 1 || this.b>80){
        this.bState = false;
      }else this.bState = true;

      if (!numRe.test(this.c)){
        this.cState = false;
      }else if(this.c < 1 || this.c>90){
        this.cState = false;
      }else this.cState = true;

    },
    computeSalary() {
      this.sum = 25 * this.a + 30 * this.b + 45 * this.c;
      if (this.sum <= 1000) {
        this.salary = this.sum * 0.1;
      } else if (this.sum <= 1800) {
        this.salary = this.sum * 0.15;
      } else {
        this.salary = this.sum * 0.2;
      }
    },
    onSubmit() {
      this.judgeInput();
      if(this.aState && this.bState && this.cState){
        this.computeSalary();
      }else{
        this.salary = "";
      }
      
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
  mounted () {
    let result='| 1    | 1        | 1          | 1        | 100      | 10     |\n' +
      '| 2    | 2        | 1          | 1        | 125      | 12.5   |\n' +
      '| 3    | 5        | 5          | 5        | 500      | 50     |\n' +
      '| 4    | 9        | 10         | 10       | 975      | 97.5   |\n' +
      '| 5    | 10       | 10         | 10       | 1000     | 100    |\n' +
      '| 6    | 11       | 10         | 10       | 1025     | 153.75 |\n' +
      '| 7    | 14       | 14         | 14       | 1400     | 210    |\n' +
      '| 8    | 17       | 18         | 18       | 1775     | 266.25 |\n' +
      '| 9    | 18       | 18         | 18       | 1800     | 270    |\n' +
      '| 10   | 19       | 18         | 18       | 1825     | 365    |\n' +
      '| 11   | 35       | 40         | 45       | 4100     | 820    |\n' +
      '| 12   | 69       | 80         | 90       | 8175     | 1635   |\n' +
      '| 13   | 70       | 80         | 90       | 8200     | 1640   | '
    let resarray=result.split('\n')
    for (var single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items.push({
        序号:temp[1],
        主机销量:temp[2],
        显示器销量:temp[3],
        外设销量:temp[4],
        销售总额:temp[5],
        佣金:temp[6]
      })
    }
    result='| 14     | 1        | 40         | 45       | 3250     | 650     |\n' +
      '| 15     | 2        | 40         | 45       | 3275     | 655     |\n' +
      '| **16** | **35**   | **40**     | **45**   | **4100** | **820** |\n' +
      '| 17     | 69       | 40         | 45       | 4950     | 990     |\n' +
      '| 18     | 70       | 40         | 45       | 4975     | 995     |\n' +
      '| 19     | 35       | 1          | 45       | 2930     | 586     |\n' +
      '| 20     | 35       | 2          | 45       | 2960     | 592     |\n' +
      '| 21     | 35       | 79         | 45       | 5270     | 1054    |\n' +
      '| 22     | 35       | 80         | 45       | 5300     | 1060    |\n' +
      '| 23     | 35       | 40         | 1        | 2120     | 424     |\n' +
      '| 24     | 35       | 40         | 2        | 2165     | 433     |\n' +
      '| 25     | 35       | 40         | 89       | 6080     | 1216    |\n' +
      '| 26     | 35       | 40         | 90       | 6120     | 1224    |'
    resarray=result.replaceAll('*','').split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items2.push({
        序号:temp[1],
        主机销量:temp[2],
        显示器销量:temp[3],
        外设销量:temp[4],
        销售总额:temp[5],
        佣金:temp[6]
      })
    }
    result='| 27   | -1       | 40         | 45       | 系统计算佣金 |\n' +
      '| 28   | 0        | 40         | 45       | 销量超出范围 |\n' +
      '| 29   | 71       | 40         | 45       | 销量超出范围 |\n' +
      '| 30   | 35       | -1         | 45       | 销量超出范围 |\n' +
      '| 31   | 35       | 0          | 45       | 销量超出范围 |\n' +
      '| 32   | 35       | 81         | 45       | 销量超出范围 |\n' +
      '| 33   | 35       | 40         | -1       | 销量超出范围 |\n' +
      '| 34   | 35       | 40         | 0        | 销量超出范围 |\n' +
      '| 35   | 35       | 40         | 91       | 销量超出范围 |'
    resarray=result.replaceAll('*','').split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      this.items4.push({
        序号:temp[1],
        主机销量:temp[2],
        显示器销量:temp[3],
        外设销量:temp[4],
        佣金:temp[5],
      })
    }
  }
};

</script>

<style scoped>
.title h1 {
  font-size: 36px;
}

.input-separator {
  height: 30px;
}
</style>
