<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="关注" name="first">
            <div>
                <div style="display:flex">
                    <iframe src="/static/report/Follow单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">关注</span></div>
                        <img :src="require('@/assets/follow_follow.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            </div>
        </el-tab-pane>
        <el-tab-pane label="取关" name="second">
            <div style="display:flex">
                    <iframe src="/static/report/Follow单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">取关</span></div>
                        <img :src="require('@/assets/follow_unfollow.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            
        </el-tab-pane>
        <el-tab-pane label="查询是否关注" name="third">
            <div style="display:flex">
                    <iframe src="/static/report/Follow单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">查询是否关注</span></div>
                        <img :src="require('@/assets/follow_find.png')" style="width: 100%;margin-top:15px">
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
