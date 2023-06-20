<template>
    <div style="display:flex">
        <iframe src="/static/report/Sys_Test_case_fun_023系统测试报告.html" style="width:70%;height:1500px"></iframe>
        <div style="margin-left:30px;margin-top:30px;">
            <div>
                <span style="font-size:30px">事件流分析：</span>
            </div>
            <div class="tableTitle"><span class="midText">场景法</span></div>
            <img :src="require('@/assets/系统测试场景2.png')" style="width: 70%;margin-top:15px">
        </div>
    </div>
</template>
<script>
export default {
data() {
    return {
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
margin-left:70px;
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
