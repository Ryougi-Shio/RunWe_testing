<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <div>
      <img src="../../../../assets/user集成1.png" class="img"/>
      <img src="../../../../assets/user集成2.png" class="img"/>
      <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>User模块 集成测试环节</span>
        <el-button style="float: right; padding: 3px 0" type="text">进行测试</el-button>
      </div>
      <div v-for="o in 5" :key="o" class="text item">
        {{content_userTest[o]}}
      </div>
      </el-card>
      <div class="answer">生成的测试报告如下：</div>
        <div style="width:100%;height:100%">
          <iframe id="html"  style="width:90%;height:850px"></iframe>
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
</style>
    
<script>
import axios from "axios";

      export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name:'User',
        data() {
          return {
            content_userTest:["","在User集成测试中，主要对UserController进行测试，主要有以下接口",
            "1. POST /user接口","2. PUT /user接口","3. /SearchUser接口","4. DELETE /user/{id}接口"]
          }
        },
        methods: {
        handleClick() {
        let param = new FormData();
        param.append("test","article")
        //console.log(param.get("test"))

        let config={
          headers: { "Content-Type": "multipart/form-data" },
        }
        axios
          .post("http://127.0.0.1:8000/do", param, config)
          .then((response) => {
            // eslint-disable-next-line no-console
            console.log(response);
            if (response['data']=="True"){
            document.getElementById("html").src="/static/report/UserController测试报告.html";
            // eslint-disable-next-line no-console
            console.log("ok")
        }

          });
        }
    },
      };
</script>
    