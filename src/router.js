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
        path: '/indexHomework',
        name: 'indexHomework',
        component: () =>
            import('./views/pages/homework/homework.vue')
    },
    ],
})

