<template>

  
<b-card>
    <div class="input-separator"></div>

    <img src="../../../img/atm.png" alt="ATM系统状态图" class="img-fluid">

    <div class="input-separator"></div>

    <b-button style="margin-left: 2vw" v-b-modal.modal0 variant="dark">穿越0个状态的测试用例</b-button>
    <b-button style="margin-left: 2vw" v-b-modal.modal1 variant="dark">穿越1个状态的测试用例</b-button>

    <b-modal size="xl" id="modal0" title="穿越0个状态的测试用例" hide-footer><b-table :items="items"></b-table></b-modal>
    <b-modal size="xl" id="modal1" title="穿越1个状态的测试用例" hide-footer><b-table :items="items2"></b-table> </b-modal>
  
</b-card>

</template>

<script>
/* eslint-disable*/
export default {
  name: 'ATM',
  data(){
    return{
      items: [],
      items2:[]
    }
  },
  mounted () {
    let result='1|启动|插卡|登陆界面\n' +
      '2|登陆界面|输入密码不正确|登陆界面\n' +
      '3|登陆界面|密码验证正确|主界面\n' +
      '4|主界面|退卡|启动\n' +
      '5|主界面|点击查看账户余额|查看余额\n' +
      '6|查看余额|点击返回|主界面\n' +
      '7|主界面|进入打印凭条|打印凭条\n' +
      '8|打印凭条|点击返回|主界面\n' +
      '9|主界面|进入存款|存款\n' +
      '10|存款|点击返回|主界面\n' +
      '11|主界面|进入转账|转账\n' +
      '12|转账|点击返回|主界面\n' +
      '13|主界面|进入取款|取款\n' +
      '14|取款|点击返回|主界面\n' +
      '15|转账|匹配卡号和判断金额|事务处理\n' +
      '16|取款|比较取款金额和存款金额|事务处理\n' +
      '17|事务处理|确认转账|转账\n' +
      '18|事务处理|进入取款|取款\n' +
      '19|登陆界面|退卡|启动'
    let resarray=result.split('\n')
    for (var single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items.push({
        序号:temp[0],
        前提:temp[1],
        测试用例描述:temp[2],
        预期结果:temp[3]
      })
    }
    result='1|启动|插卡且输入密码不正确|登陆界面\n' +
      '2|登陆界面|输入两次密码都不正确|登陆界面\n' +
      '3|登陆界面|输入密码不正确后退卡|启动\n' +
      '4|登陆界面|第一次输入密码不正确，第二次输入密码正确|主界面\n' +
      '5|登陆界面|输入密码正确并退卡|启动\n' +
      '6|登陆界面|输入密码正确后点击查看账户余额|查看余额\n' +
      '7|登陆界面|输入密码正确后进入转账|转账\n' +
      '8|登陆界面|输入密码正确后进入取款|取款\n' +
      '9|登陆界面|输入密码正确后进入存款|存款\n' +
      '10|登陆界面|输入密码正确后进入打印凭条|打印凭条\n' +
      '11|主界面|查看账户余额后返回|主界面\n' +
      '12|主界面|进入存款后返回|主界面\n' +
      '13|主界面|进入打印凭条后返回|主界面\n' +
      '14|主界面|进入转账后返回|主界面\n' +
      '15|主界面|进入转账后匹配可好和判断金额|事务处理\n' +
      '16|主界面|进入取款后返回|主界面\n' +
      '17|主界面|进入取款后比较取款金额和存款金额|事务处理\n' +
      '18|转账|匹配卡号和判断金额后确认转账|转账\n' +
      '19|取款|比较取款金额和存款金额后进入取款|取款'
    resarray=result.split('\n')
    for (single in resarray){
      let temp=resarray[single].split('|')
      console.log(temp)
      this.items2.push({
        序号:temp[0],
        前提:temp[1],
        测试用例描述:temp[2],
        预期结果:temp[3]
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
