import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
        redirect: '/aa',

    }, {
        path: '/aa',
        name: 'aa',
        component: () =>
            import('./views/aa.vue')
    },
    {
        path: '/articleIntegration',
        name: 'articleIntegration',
        component: () =>
            import('./views/pages/project/integrationtesting/Article.vue')
    },
    {
        path: '/followIntegration',
        name: 'followIntegration',
        component: () =>
            import('./views/pages/project/integrationtesting/Follow.vue')
    },
    {
        path: '/managerIntegration',
        name: 'managerIntegration',
        component: () =>
            import('./views/pages/project/integrationtesting/Manager.vue')
    },
    {
        path: '/userIntegration',
        name: 'userIntegration',
        component: () =>
            import('./views/pages/project/integrationtesting/User.vue')
    },
    {
        path: '/performanceTest',
        name: 'performanceTest',
        component: () =>
            import('./views/pages/project/systemtesting/performanceTest.vue')
    },
    {
        path: '/articleSystem',
        name: 'articleSystem',
        component: () =>
            import('./views/pages/project/systemtesting/article.vue')
    },
    {
        path: '/userSystem',
        name: 'userSystem',
        component: () =>
            import('./views/pages/project/systemtesting/user.vue')
    },
    {
        path: '/followSystem',
        name: 'followSystem',
        component: () =>
            import('./views/pages/project/systemtesting/follow.vue')
    },
    {
        path: '/managerSystem',
        name: 'managerSystem',
        component: () =>
            import('./views/pages/project/systemtesting/manager.vue')
    },
    {
        path: '/ATM',
        name: 'ATM',
        component: () =>
            import('./views/pages/homework/ATM.vue')
    },
    {
        path: '/DianXinFeiYong',
        name: 'DianXinFeiYong',
        component: () =>
            import('./views/pages/homework/DianXinFeiYong.vue')
    },
    {
        path: '/Triangle',
        name: 'Triangle',
        component: () =>
            import('./views/pages/homework/Triangle.vue')
    },
    {
        path: '/WanNianLi',
        name: 'WanNianLi',
        component: () =>
            import('./views/pages/homework/WanNianLi.vue')
    },
    {
        path: '/WhiteBox',
        name: 'WhiteBox',
        component: () =>
            import('./views/pages/homework/WhiteBox.vue')
    },
    {
        path: '/YongJin',
        name: 'YongJin',
        component: () =>
            import('./views/pages/homework/YongJin.vue')
    },
    {
        path: '/userunit',
        name: 'userunit',
        component: () =>
            import('./views/pages/project/unittesting/user.vue')
    },
    {
        path: '/followunit',
        name: 'followunit',
        component: () =>
            import('./views/pages/project/unittesting/follow.vue')
    },
    {
        path: '/managerunit',
        name: 'managerunit',
        component: () =>
            import('./views/pages/project/unittesting/manager.vue')
    },
    {
        path: '/articleunit',
        name: 'articleunit',
        component: () =>
            import('./views/pages/project/unittesting/article.vue')
    },
    ],
})

