<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <div>
      <img src="../../../../assets/article集成.png" class="img"/>
      <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>Article模块 集成测试环节</span>
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
        name:'Article',
        data() {
          return {
            content_userTest:["","在Article集成测试中，主要对ArticleController进行测试，主要有以下接口",
            "1. /article/like接口","2. /article/{id}接口","3. /article接口"]
          }
        }
      };
</script>
    