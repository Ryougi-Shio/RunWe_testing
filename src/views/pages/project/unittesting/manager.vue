<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="加入俱乐部" name="first">
            <div>
                <img :src="require('@/assets/manager_join.png')" alt="关注" style="width: 50%; height: 300px;">
            </div>
        </el-tab-pane>
        <el-tab-pane label="删除成员" name="second">
            <img :src="require('@/assets/manager_delete.png')" alt="取关" style="width: 50%; height: 400px;">
        </el-tab-pane>
        <el-tab-pane label="返回部分指定成员" name="third">
            <img :src="require('@/assets/manager_part.png')" alt="查询是否关注" style="width: 50%; height: 300px;">
        </el-tab-pane>
        <el-tab-pane label="返回某个指定成员的社团关联表" name="fourth">
            <img :src="require('@/assets/manager_link.png')" alt="查询是否关注" style="width: 50%; height: 300px;">
        </el-tab-pane>
        <el-tab-pane label="返回某个指定用户的关注社团" name="fifth">
            <img :src="require('@/assets/manager_like.png')" alt="查询是否关注" style="width: 50%; height: 300px;">
        </el-tab-pane>
        <el-tab-pane label="更改社团中用户权限" name="sixth">
            <img :src="require('@/assets/manager_user.png')" alt="查询是否关注" style="width: 50%; height: 300px;">
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
            console.log(tab, event);
        }
    },
};
</script>

