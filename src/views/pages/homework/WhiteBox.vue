<template>

  <b-jumbotron style="height: 800px" header="白盒测试问题" class="title">

    <div class="input-separator"></div>

    <img src="../../../img/whitebox.png" alt="流程图" class="img-fluid">

    <div class="input-separator"></div>

    <b-button style="margin-left: 2vw" v-b-modal.modal0 variant="dark">语句覆盖</b-button>
    <b-button style="margin-left: 2vw" v-b-modal.modal1 variant="dark">判断覆盖</b-button>
    <b-button style="margin-left: 2vw" v-b-modal.modal2 variant="dark">条件覆盖</b-button>
    <b-button style="margin-left: 2vw" v-b-modal.modal3 variant="dark">判断-条件覆盖</b-button>
    <b-button style="margin-left: 2vw" v-b-modal.modal4 variant="dark">条件组合覆盖</b-button>

    <b-modal size="xl" id="modal0" title="语句覆盖" hide-footer><b-table :items="items"></b-table></b-modal>
    <b-modal size="xl" id="modal1" title="判断覆盖" hide-footer><b-table :items="items2"></b-table> </b-modal>
    <b-modal size="xl" id="modal2" title="条件覆盖" hide-footer><b-table :items="items3"></b-table> </b-modal>
    <b-modal size="xl" id="modal3" title="判断-条件覆盖" hide-footer><b-table :items="items4"></b-table> </b-modal>
    <b-modal size="xl" id="modal4" title="条件组合覆盖" hide-footer><b-table :items="items5"></b-table> </b-modal>

  </b-jumbotron>
</template>

<script>
/* eslint-disable*/
export default {
  name: 'WhiteBox',
  data(){
    return{
      items:[],
      items2:[],
      items3:[],
      items4:[],
      items5:[]
    }
  },
  mounted () {
    let result='CASE1|年销售额大于200万，请假天数不大于10天，现金到账大于等于60%|OACG\n' +
      'CASE2|年销售额大于200万，请假天数不大于10天，现金到账小于60%|OADG\n' +
      'CASE3|年销售额小于200万，请假天数不大于10天，现金到账大于85%|OBFG\n' +
      'CASE4|年销售额小于200万，请假天数不大于10天，现金到账小于等于85%|OBEG'
    let resarray=result.split('\n')
    for (var single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items.push({
        测试用例名称:temp[0],
        测试用例描述:temp[1],
        测试路径:temp[2],
      })
    }
    result='CASE1|年销售额大于200万，请假天数不大于10天，现金到账大于等于60%|O真A真\n' +
      'CASE2|年销售额大于200万，请假天数不大于10天，现金到账小于60%|O真A假\n' +
      'CASE3|年销售额小于200万，请假天数不大于10天，现金到账大于85%|O假B真\n' +
      'CASE4|年销售额小于200万，请假天数不大于10天，现金到账小于等于85%|O假B假'
    resarray=result.split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items2.push({
        测试用例名称:temp[0],
        测试用例描述:temp[1],
        覆盖判定:temp[2],
      })
    }
    result='CASE1|210W|9|70%|OACG|T1T2T3\n' +
      'CASE2|220W|10|50%|OADG|T1T2F3\n' +
      'CASE3|220W|11|89%|OBFG|T1F2T4\n' +
      'CASE4|190W|8|83%|OBEG|F1T2F4'
    resarray=result.split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items3.push({
        测试用例名称:temp[0],
        年销售额:temp[1],
        请假天数:temp[2],
        现金到账:temp[3],
        所走路径:temp[4],
        覆盖条件:temp[5]
      })
    }
    result='CASE1|210W|9|70%|OACG|AC|T1T2T3\n' +
      'CASE2|220W|10|50%|OADG|AD|T1T2F3\n' +
      'CASE3|220W|11|89%|OBFG|BF|T1F2T4\n' +
      'CASE4|190W|8|83%|OBEG|BE|F1T2F4'
    resarray=result.split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items4.push({
        测试用例名称:temp[0],
        年销售额:temp[1],
        请假天数:temp[2],
        现金到账:temp[3],
        所走路径:temp[4],
        覆盖分支:temp[5],
        覆盖条件:temp[6]
      })
    }
    result='CASE1|210W|9|70%|OACG|T1T2T3\n' +
      'CASE2|220W|10|50%|OADG|T1T2F3\n' +
      'CASE3|220W|11|89%|OBFG|T1F2T4\n' +
      'CASE4|22OW|12|82%|OBEG|T1F2F4\n' +
      'CASE5|190W|9|89%|OBFG|F1T2T4\n' +
      'CASE6|190W|9|83%|OBEG|F1T2F4\n' +
      'CASE7|190W|12|89%|OBFG|F1F2T4\n' +
      'CASE8|190W|13|83%|OBEG|F1F2F4'
    resarray=result.split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items5.push({
        测试用例名称:temp[0],
        年销售额:temp[1],
        请假天数:temp[2],
        现金到账:temp[3],
        所走路径:temp[4],
        覆盖条件:temp[5]
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
