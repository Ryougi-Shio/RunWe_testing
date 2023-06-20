<template>
    <div>
    <b-jumbotron style="height: 80px" header="判断三角形类型问题" class="title">
  </b-jumbotron>
  <div STYLE="display:flex">
      <el-card style="width:45%;height:400px" class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-size:20px;font-weight:bold;">验证部分</span>
      <el-button style="font-size:20px;font-weight:bold;float: right; padding: 3px 0" @click="onsubmit" type="text">进行测试</el-button>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>第一条边: </b-input-group-prepend>
      <b-form-input v-model.number="a" type="number" placeholder="请输入第一条边(1~100)"></b-form-input>
    </b-input-group>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div>
      <b-input-group>
      <b-input-group-prepend is-text>第二条边: </b-input-group-prepend>
      <b-form-input v-model.number="b" type="number" placeholder="请输入第二条边(1~100)"></b-form-input>
    </b-input-group>
    </div>
    <div class="input-separator"></div>
    <div>
      <b-input-group>
        <b-input-group-prepend is-text>第三条边: </b-input-group-prepend>
        <b-form-input v-model.number="c" type="number" placeholder="请输入第三条边(1~100)"></b-form-input>
      </b-input-group>
    </div>
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
        <b-dropdown-item  @click="changeTable(1)">基本边界值</b-dropdown-item>
        <b-dropdown-item  @click="changeTable(2)">健壮性边界值</b-dropdown-item>
      </b-dropdown>
    </div>
    <div>
      <div class="input-separator"></div>
    </div>
    <div>
      <b-dropdown style="margin-left: 2vw" text="等价类" variant="dark"  @click="handleClick">
      <b-dropdown-item  @click="changeTable(4)">有效等价类</b-dropdown-item>
      <b-dropdown-item  @click="changeTable(5)">无效等价类</b-dropdown-item>
    </b-dropdown>
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
        prop="第一条边"
        label="第一条边"
        width="300">
      </el-table-column>
      <el-table-column
        prop="第二条边"
        label="第二条边"
        width="300">
      </el-table-column>
      <el-table-column
        prop="第三条边"
        label="第三条边"
        width="300">
      </el-table-column>
      <el-table-column
        prop="输出"
        label="输出"
        width="400">
      </el-table-column>
      <el-table-column
        prop="输入类型"
        label="输入类型"
        width="400">
      </el-table-column>
    </el-table>
  </el-card>
  </div>
  </div>
</template>

<script>
import Trangle from '@/util/Trangle';
/* eslint-disable*/
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Triangle',
  data() {
    return {
      items: [],
      items2: [],
      items3: [],
      items4: [],
      items5: [],
      targetTable: [],
      result: "",
    }
  },
  methods: {
    onsubmit() {
      this.result = Trangle(this.a, this.b, this.c)
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
    let result = '1 | 1 | 1 | 1 | 等边三角形 | 输入三条相等的最小边长\n'+
'2 | 100 | 100 | 100 | 等边三角形 | 输入三条相等的最大边长\n'+
'3 | 1 | 2 | 2 | 无法构成三角形 | 输入两种相等的最小边长\n'+
'4 | 2 | 3 | 4 | 普通三角形 | 第一条边长为最小边界值，其他边长在范围内\n'+
'5 | 99 | 100 | 100 | 等腰三角形 | 第一条边长为最大边界值减一，其他边长在范围内\n'+
'6 | 100 | 99 | 99 | 等腰三角形 | 第二条边长为最大边界值减一，其他边长在范围内\n'+
'7 | 98 | 99 | 100 | 普通三角形 | 第三条边长为最大边界值减一，其他边长在范围内\n'+
'8 | 1 | 100 | 100 | 无法构成三角形 | 第一条边长为最小边界值，其他边长在范围内\n'+
'9 | 100 | 1 | 100 | 无法构成三角形 | 第二条边长为最小边界值，其他边长在范围内\n'+
'10 | 100 | 100 | 1 | 无法构成三角形 | 第三条边长为最小边界值，其他边长在范围内\n'

    let resarray = result.split('\n')
    for (var single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items.push({
        序号: temp[0],
        第一条边: temp[1],
        第二条边: temp[2],
        第三条边: temp[3],
        输出: temp[4],
        输入类型: temp[5],
      })
    }
    result = '11 | 0 | 50 | 50 | 无法构成三角形 | 第一条边长为最小边界值减一\n'+
'12 | 101 | 50 | 50 | 无法构成三角形 | 第一条边长为最大边界值加一\n'+
'13 | -1 | 50 | 50 | 边超出范围 | 第一条边长为负数\n'+
'14 | 50 | 0 | 50 | 无法构成三角形 | 第二条边长为最小边界值减一\n'+
'15 | 50 | 101 | 50 | 边超出范围 | 第二条边长为最大边界值加一\n'+
'16 | 50 | -1 | 50 | 边超出范围 | 第二条边长为负数\n'+
'17 | 50 | 50 | 0 | 无法构成三角形 | 第三条边长为最小边界值减一\n'+
'18 | 50 | 50 | 101 | 边超出范围 | 第三条边长为最大边界值加一\n'+
'19 | 50 | 50 | -1 | 边超出范围 | 第三条边长为负数\n'
    resarray = result.split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      console.log(temp)
      this.items2.push({
        序号: temp[0],
        第一条边: temp[1],
        第二条边: temp[2],
        第三条边: temp[3],
        输出: temp[4],
        输入类型: temp[5],
      })
    }
    result = '20 | 3 | 4 | 5 | 普通三角形 | 长度符合构成三角形的规则，能构成三角形\n'+
'21 | 4 | 4 | 4 | 等边三角形 | 三条边长度相等，构成等边三角形\n'+
'22 | 4 | 4 | 5 | 等腰三角形 | 两条边长度相等，构成等腰三角形\n'+
'23 | 4 | 5 | 6 | 普通三角形 | 长度符合构成三角形的规则，能构成三角形\n'
    resarray = result.replaceAll('*', '').split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      this.items4.push({
        序号: temp[0],
        第一条边: temp[1],
        第二条边: temp[2],
        第三条边: temp[3],
        输出: temp[4],
        输入类型: temp[5],
      })
    }
    result = '24 | 2 | 2 | 4 | 无法构成三角形 | 其中两条边的长度之和等于第三边\n'+
'25 | 5 | 1 | 1 | 无法构成三角形 | 其中两条边的长度之和小于第三边\n'+
'26 | 100 | 1 | 1 | 无法构成三角形 | 其中两条边的长度之和小于第三边\n'+
'27 | 4 | 10 | 4 | 无法构成三角形 | 其中两条边的长度之和小于第三边\n'
    resarray = result.replaceAll('*', '').split('\n')
    for (single in resarray) {
      let temp = resarray[single].split('|')
      this.items5.push({
        序号: temp[0],
        第一条边: temp[1],
        第二条边: temp[2],
        第三条边: temp[3],
        输出: temp[4],
        输入类型: temp[5],
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
