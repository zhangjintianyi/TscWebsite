import Vue from 'vue'
import Router from 'vue-router'
import LabEnv from '@/components/LabEnv'
import LabEnvTable from '@/components/LabEnvTable'
import Documents from '@/components/Documents'
import EnvTopo from '@/components/LabEnvTopoOuter'
import UserInfo from '@/components/UserInfo';
import Login from '@/components/Login';
import Message from '@/components/Message';
import MessageInfo from '@/components/MessageInfo';
import MessagePublish from '@/components/MessagePublish';
import AppMain from '@/components/AppMain';
import store from '@/store'

Vue.use(Router)

const router = new Router({
  routes: [{
      path: '/',
      redirect: '/environment',
      component: AppMain,
      children: [{
          path: 'environment',
          name: 'LabEnvTable',
          component: LabEnvTable
        },
        {
          path: 'environment/simple',
          name: 'LabEnvSimple',
          component: LabEnv
        },
        {
          path: 'doc',
          name: 'Document',
          component: Documents
        },
        {
          path: 'topo',
          name: 'Topo',
          component: EnvTopo
        },
        {
          path: 'user',
          name: 'User',
          component: UserInfo
        },
        {
          path: 'message/',
          name: 'Message',
          component: Message,
        },
        {
          path: 'message/info',
          name: 'MessageInfo',
          component: MessageInfo,
        },
        {
          path: 'message/publish',
          name: 'MessagePublish',
          component: MessagePublish,
        },
      ]
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
  ]
})
router.beforeEach((to, from, next) => {
  //to and from are Route Object,next() must be called to resolve the hook
  if (store.getters.token) {
    console.log(store.getters.token)
    if (to.path === "/login") {
      next('/environment');
    }
    next();
  } else {
    if (to.path === "/login") {
      next();
    } else {
      next("/login");
    }
  }

});

export default router;
