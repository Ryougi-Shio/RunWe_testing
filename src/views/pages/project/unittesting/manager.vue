<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="加入俱乐部" name="first">
            <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">加入俱乐部</span></div>
                        <img :src="require('@/assets/manager_join.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            
        </el-tab-pane>
        <el-tab-pane label="删除成员" name="second">
            <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">删除成员</span></div>
                        <img :src="require('@/assets/manager_delete.png')" style="width: 70%;margin-top:15px">
                    </div>
                </div>
        </el-tab-pane>
        <el-tab-pane label="返回部分指定成员" name="third">
            <div style="display:flex">
                    <iframe src="/static/report/Article单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">返回部分指定成员</span></div>
                        <img :src="require('@/assets/manager_part.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
        </el-tab-pane>
        <el-tab-pane label="返回某个指定成员的社团关联表" name="fourth">
            <div style="display:flex">
                    <iframe src="/static/report/Manager单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">返回某个指定成员的社团关联表</span></div>
                        <img :src="require('@/assets/manager_link.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
        </el-tab-pane>
        <el-tab-pane label="返回某个指定用户的关注社团" name="fifth">
            <div style="display:flex">
                    <iframe src="/static/report/Manager单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">返回某个指定用户的关注社团</span></div>
                        <img :src="require('@/assets/manager_like.png')" style="width: 50%;margin-top:15px">
                    </div>
                </div>
            
        </el-tab-pane>
        <el-tab-pane label="更改社团中用户权限" name="sixth">
            <div style="display:flex">
                    <iframe src="/static/report/Manager单元测试报告.html" style="width:50%;height:1500px"></iframe>
                    <div style="margin-left:30px;margin-top:30px;">
                        <div>
                            <span style="font-size:30px">测试用例：</span>
                        </div>
                        <div class="tableTitle"><span class="midText">更改社团中用户权限</span></div>
                        <img :src="require('@/assets/manager_user.png')" style="width: 70%;margin-top:15px">
                    </div>
                </div>
            
        </el-tab-pane>
    </el-tabs>
</template>
<script>
export default {
    data() {
        return {
            activeName: 'second'
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
