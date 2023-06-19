<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div >
      <div >
        <img src="../../../../assets/follow集成.png" class="img"/>
        <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>Follow模块 集成测试环节</span>
          <el-button style="float: right; padding: 3px 0" type="text">进行测试</el-button>
        </div>
        <div v-for="o in 5" :key="o" class="text item">
          {{content_userTest[o]}}
        </div>
        </el-card>
        <div class="answer">生成的测试报告如下：</div>
        <div style="width:100%;height:100%">
          <iframe src="/static/report/FollowController测试报告.html" style="width:90%;height:850px"></iframe>
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
            width:70%
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
          name:'Follow',
          data() {
            return {
              content_userTest:["","在Follow集成测试中，主要对FollowController进行测试，主要有以下接口",
              "1. /follow接口","2. /follow/{id}接口","3. /follow/common/{id}接口", "4. /follow/or/not/{followUserId}接口"],
            }
          },
        };
  </script>
      