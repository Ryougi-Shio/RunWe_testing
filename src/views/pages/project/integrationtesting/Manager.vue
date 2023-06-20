<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div>
        <img src="../../../../assets/manager集成.png" class="img"/>
        <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>Manager模块 集成测试环节</span>
          <el-button style="float: right; padding: 3px 0" type="text">进行测试</el-button>
        </div>
        <div v-for="o in 7" :key="o" class="text item">
          {{content_userTest[o]}}
        </div>
        </el-card>
        <div class="answer">生成的测试报告如下：</div>
        <div style="width:100%;height:100%">
          <iframe src="/static/report/ManagerController测试报告.html" style="width:90%;height:650px"></iframe>
        </div>
      </div>
    </div>
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
          font-size:30px;
          font-weight:bold;
          margin-bottom:10px;
        }
  </style>
      
  <script>
        export default {
          // eslint-disable-next-line vue/multi-word-component-names
          name:'Manager',
          data() {
            return {
              content_userTest:["","在Manager集成测试中，主要对ManagerController进行测试，主要有以下接口",
              "1. /changeRank接口","2. /getClub/{user_id}接口","3. /getRank/{user_id}/{as_id}接口",
               "4. POST /manager接口","5. DELETE /manager接口","6. GET /manager/{as_id}/{rank}接口"],
              src: require('@/assets/follow集成.png')
            }
          }
        };
  </script>
      