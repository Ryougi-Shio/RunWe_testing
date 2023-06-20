<template>
  <div>
    <el-menu background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" :default-active="activeIndex" router
      style="min-height:100vh;width:230px;float:left">
      <NavMenu :navMenus="menuData"></NavMenu>
    </el-menu>
    <router-view style="margin-left:250px"></router-view>
  </div>
</template>

<script>
import NavMenu from "./components/NavMenu.vue";
export default {
  components: {
    NavMenu: NavMenu
  },
  data() {
    return {
      activeIndex: 'aa',
      menuData: [

        {
          //一级
          entity: {
            id: 0,
            name: "top1",
            icon: "el-icon-message",
            alias: "作业模块"
          },
          //二级
          childs: [
            {
              entity: {
                id: 1,
                name: "indexHomework",
                icon: "el-icon-loading",
                alias: "作业首页"
              }
            }
          ]
        },
        {
          //一级，项目模块
          entity: {
            id: 2,
            name: "top2",
            icon: "el-icon-message",
            alias: "项目测试模块"
          },
          //二级，单元测试
          childs: [
            {
              entity: {
                id: 3,
                name: "top2_1",
                icon: "el-icon-loading",
                alias: "单元测试"
              },
              //三级
              childs: [
                {
                  entity: {
                    id: 4,
                    name: "userunit",
                    icon: "el-icon-sold-out\r\n",
                    alias: "User模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 5,
                    name: "articleunit",
                    icon: "el-icon-service\r\n",
                    alias: "Article模块",
                    value: "/content/pass"
                  }
                },
                {
                  entity: {
                    id: 6,
                    name: "followunit",
                    icon: "el-icon-sold-out\r\n",
                    alias: "Follow模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 7,
                    name: "managerunit",
                    icon: "el-icon-service\r\n",
                    alias: "Manager模块",
                    value: "/content/pass"
                  }
                }
              ]
            },
            //二级，集成测试模块
            {
              entity: {
                id: 8,
                name: "top2_2",
                icon: "el-icon-loading",
                alias: "集成测试"
              },
              //三级
              childs: [
                {
                  entity: {
                    id: 9,
                    name: "userIntegration",
                    icon: "el-icon-sold-out\r\n",
                    alias: "User模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 10,
                    name: "articleIntegration",
                    icon: "el-icon-service\r\n",
                    alias: "Article模块",
                    value: "/content/pass"
                  }
                },
                {
                  entity: {
                    id: 11,
                    name: "followIntegration",
                    icon: "el-icon-sold-out\r\n",
                    alias: "Follow模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 12,
                    name: "managerIntegration",
                    icon: "el-icon-service\r\n",
                    alias: "Manager模块",
                    value: "/content/pass"
                  }
                }
              ]
            },
            //二级，系统测试模块
            {
              entity: {
                id: 13,
                name: "top2_3",
                icon: "el-icon-loading",
                alias: "系统测试"
              },
              //三级
              childs: [
                {
                  entity: {
                    id: 14,
                    name: "performanceTest",
                    icon: "el-icon-sold-out\r\n",
                    alias: "性能及压力测试",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 15,
                    name: "userSystem",
                    icon: "el-icon-sold-out\r\n",
                    alias: "User模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 16,
                    name: "articleSystem",
                    icon: "el-icon-sold-out\r\n",
                    alias: "Article模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 15,
                    name: "followSystem",
                    icon: "el-icon-sold-out\r\n",
                    alias: "Follow模块",
                    value: "/content/email"
                  }
                },
                {
                  entity: {
                    id: 15,
                    name: "managerSystem",
                    icon: "el-icon-sold-out\r\n",
                    alias: "Manager模块",
                    value: "/content/email"
                  }
                },
              ]
            }
          ],
        },
      ],

    };
  },
  mounted() {
    // eslint-disable-next-line no-console
    console.log(window.location.href)
    let start = window.location.href.lastIndexOf('/');
    let path = window.location.href.slice(start + 1);
    this.activeIndex = path;

    // eslint-disable-next-line no-console
    console.log(this.activeIndex)
  }

};
</script>

<style></style>