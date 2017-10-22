import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';
import getters from './getter'
import user from './modules/user';
import message from './modules/message';

Vue.use(Vuex);

const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage
  })],
  modules: {
    user, message,
  },
  state: {
    simpleSwitchOn: false,
    jobNum: null,

  },
  mutations: {
    changeSimpleSwitch(state) {
      state.simpleSwitchOn = !state.simpleSwitchOn;
    },
    changeAvatarSrc(state, newAvatarSrc) {
      state.avatarSrc = newAvatarSrc;
    },
  },
  actions: {
    ToggleSimpleSwitch: ({
      commit
    }) => {
      commit("changeSimpleSwitch");
    },
    ToggleAvatarSrc: (context) => {
      context.commit("changeAvatarSrc", context.newAvatarSrc);
    }
  },
  getters
})

export default store;
