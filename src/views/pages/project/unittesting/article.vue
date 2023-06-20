<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="点赞/取消点赞文章" name="first">
            <div>
                <img :src="require('@/assets/article_like.png')" style="width: 50%; height: 300px;">
            </div>
        </el-tab-pane>
        <el-tab-pane label="查询文章" name="second">
            <img :src="require('@/assets/article_find.png')" style="width: 50%; height: 400px;">
        </el-tab-pane>
        <el-tab-pane label="创建文章" name="third">
            <img :src="require('@/assets/article_post.png')" style="width: 50%; height: 200px;">
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

