<template>
    <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
      <el-tab-pane label="登录接口性能测试" name="first">
        <div class="answer">登录性能及压力测试</div>
        <div style="margin-top:30px;width:100%;height:100%;display:flex">
          <iframe src="/static/report/登陆性能.html" style="margin-left:30px;width:50%;height:1500px"></iframe>
            <div style="margin-left:100px;width:50%;height:100%;display:flex">
                <el-progress style="margin-top:30px" stroke-width=20 width=300 type="circle" :percentage="100" status="success"></el-progress>
                <el-card style="margin-left:30px;margin-top:30px;width:50%;height:100%" class="box-card">
                <div slot="header" class="clearfix">
                    <span style="font-size:25px;font-weight:bold">报告简述</span>
                </div>
                <div v-for="o in 4" :key="o" class="text item" style="font-size:25px">
                    {{data1[o]}}
                </div>
                </el-card>
            </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="获取文章性能测试" name="second">
        <div class="answer">获取文章接口性能及压力测试</div>
        <div style="margin-top:30px;width:100%;height:100%;display:flex">
          <iframe src="/static/report/获取文章性能.html" style="margin-left:30px;width:50%;height:1500px"></iframe>
          <div style="margin-left:100px;width:50%;height:100%;display:flex">
                <el-progress style="margin-top:30px" stroke-width=20 width=300 type="circle" :percentage="100" status="success"></el-progress>
                <el-card style="margin-left:30px;margin-top:30px;width:50%;height:100%" class="box-card">
                <div slot="header" class="clearfix">
                    <span style="font-size:25px;font-weight:bold">报告简述</span>
                </div>
                <div v-for="o in 4" :key="o" class="text item" style="font-size:25px">
                    {{data2[o]}}
                </div>
                </el-card>
            </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="查询用户加入社团" name="third">
        <div class="answer">查询用户加入社团接口性能及压力测试</div>
        <div style="margin-top:30px;width:100%;height:100%;display:flex">
          <iframe src="/static/report/查询用户加入社团性能.html" style="margin-left:30px;width:50%;height:1500px"></iframe>
          <div style="margin-left:100px;width:50%;height:100%;display:flex">
                <el-progress style="margin-top:30px" stroke-width=20 width=300 type="circle" :percentage="100" status="success"></el-progress>
                <el-card style="margin-left:30px;margin-top:30px;width:50%;height:100%" class="box-card">
                <div slot="header" class="clearfix">
                    <span style="font-size:25px;font-weight:bold">报告简述</span>
                </div>
                <div v-for="o in 4" :key="o" class="text item" style="font-size:25px">
                    {{data3[o]}}
                </div>
                </el-card>
            </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </template>
    <style>
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
        width: 80%;
      }
      .img {
          width:50%
      }
      .answer {
        text-align:center;
        font-size:30px;
        font-weight:bold;
        margin-bottom:10px;
      }
</style>
  <script>
    export default {
      data() {
        return {
          activeName: 'first',
          data1:["","通过：100%-500","失败：0.00%-0","总耗时：7337.756秒","平均接口请求耗时：4788毫秒"],
          data2:["","通过：100%-500","失败：0.00%-0","总耗时：5581.241秒","平均接口请求耗时：2201毫秒"],
          data3:["","通过：100%-500","失败：0.00%-0","总耗时：6194.487秒","平均接口请求耗时：2734毫秒"]
        };
      },
      methods: {
        handleClick(tab, event) {
          // eslint-disable-next-line no-console
          console.log(tab, event);
        }
      }
    };
  </script>