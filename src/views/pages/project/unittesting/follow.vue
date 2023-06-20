<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="关注" name="first">
            <div>
                <img :src="require('@/assets/follow_follow.png')" alt="关注" style="width: 50%; height: 300px;">
            </div>
        </el-tab-pane>
        <el-tab-pane label="取关" name="second">
            <img :src="require('@/assets/follow_unfollow.png')" alt="取关" style="width: 50%; height: 400px;">
        </el-tab-pane>
        <el-tab-pane label="查询是否关注" name="third">
            <img :src="require('@/assets/follow_find.png')" alt="查询是否关注" style="width: 50%; height: 300px;">
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

