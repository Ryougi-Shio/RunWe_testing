<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <div>
      <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>User模块 集成测试环节</span>
        <el-button style="float: right; padding: 3px 0" type="text">进行测试</el-button>
      </div>
      <div v-for="o in 4" :key="o" class="text item">
        {{content_userTest[o]}}
      </div>
      </el-card>
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
      export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name:'User',
        data() {
          return {
            content_userTest:["","在User集成测试中，主要对UserController进行测试，主要有以下接口",
            "1. ","2. ","3. "]
          }
        }
      };
</script>
    