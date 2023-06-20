<template>
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="点赞/取消点赞文章" name="first">
                <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">点赞/取消点赞文章</span></div>
                        <img :src="require('@/assets/article_like.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            </el-tab-pane>
            <el-tab-pane label="查询文章" name="second">
                <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">查询文章</span></div>
                        <img :src="require('@/assets/article_find.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            </el-tab-pane>
            <el-tab-pane label="创建文章" name="third">
                <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">点赞/取消点赞文章</span></div>
                        <img :src="require('@/assets/article_post.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            </el-tab-pane>
        </el-tabs>
</template>
<script>
export default {
    data() {
        return {
            activeName: 'first'
        };
    },
    methods: {
        handleClick(tab, event) {
            // eslint-disable-next-line no-console
            console.log(tab, event);
        }
    },
};
</script>

<style>
.tableTitle {
    font-weight:bold;
    margin-top:15px;
    position: relative;
    width: 50%;
    height: 1px;
    background-color: #d4d4d4;
    text-align: center;
    font-size: 16px;
    color: rgba(101, 101, 101, 1);
  }
 .midText {
    position: absolute;
    left: 50%;
    background-color: #ffffff;
    padding: 0 15px;
    transform: translateX(-50%) translateY(-50%);
  }
</style>

