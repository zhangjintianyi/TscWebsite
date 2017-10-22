import axios from "axios";
import instance from '@/api/fetch';

const user = {
  state: {
    jobNum: "",
    username: "",
    email: "",
    mobile: "",
    phone: "",
    avatar: "",
    token: "",
    status: "", // 1位登录 0为登出
  },
  mutations: {
    SET_JOB_NUM: (state, jobNum) => {
      state.jobNum = jobNum;
    },
    SET_USERNAME: (state, username) => {
      state.username = username;
    },
    SET_EMAIL: (state, email) => {
      state.email = email;
    },
    SET_MOBILE: (state, mobile) => {
      state.mobile = mobile;
    },
    SET_PHONE: (state, phone) => {
      state.phone = phone;
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar;
    },
    SET_TOKEN: (state, token) => {
      state.token = token;
    },
    SET_STATUS: (state, status) => {
      state.status = status;
    },
    LOGIN_SUCCESS: () => {
      console.log('login success')
    },
    LOGOUT_USER: state => {
      state.user = '';
    }
  },
  actions: {
    Login({
      commit
    }, userInfo) {
      console.log(userInfo)
      const jobNum = userInfo.jobNum.trim();
      const username = userInfo.username.trim();
      const password = userInfo.password;
      const params = {
        job_num: `${jobNum}`,
        username: `${username}`,
        password: `${password}`
      };
      return new Promise((resolve, reject) => {
        axios.post("http://127.0.0.1:8000/users/", params)
          .then((response) => {
            console.log("response", response);
            const data = response.data;
            commit('SET_TOKEN', data.token);
            commit('SET_JOB_NUM', data.job_num);
            commit('SET_USERNAME', data.username);
            commit('SET_STATUS', 1);
            resolve();
          })
          .catch((error) => {
            console.log(error);
          })
      });
    },
    Logout({
      commit
    }) {},

    updateUserInfo({
      commit
    }, userInfo) {
      const jobNum = userInfo.jobNum.trim();
      const username = userInfo.username.trim();
      const email = userInfo.email.trim();
      const mobile = userInfo.mobile.trim();
      const phone = userInfo.phone.trim();
      const params = {
        job_num: `${jobNum}`,
        username: `${username}`,
        email: `${email}`,
        mobile: `${mobile}`,
        phone: `${phone}`,
      };
      instance.patch("http://127.0.0.1:8000/users/user-detail/", params)
        .then((response) => {
          console.log("response", response);
          const data = response.data;
          commit('SET_JOB_NUM', data.job_num);
          commit('SET_USERNAME', data.username);
          commit('SET_EMAIL', data.email);
          commit('SET_MOBILE', data.mobile);
          commit('SET_PHONE', data.phone);
          commit('SET_AVATAR', data.avatar);
        })
        .catch((error) => {
          console.log(error);
        })
    },

    getUserInfo({
      commit
    }, jobNum) {
      instance.get("http://127.0.0.1:8000/users/" + jobNum)
        .then((response) => {
          console.log("response1111111", response);
          const data = response.data;
          commit('SET_JOB_NUM', data.job_num);
          commit('SET_USERNAME', data.username);
          commit('SET_EMAIL', data.email);
          commit('SET_MOBILE', data.mobile);
          commit('SET_PHONE', data.phone);
          commit('SET_AVATAR', data.avatar);
        })
        .catch((error => {
          console.log(error);
        }))
    },

    getAllUserInfo({commit}) {
      return instance.get("http://127.0.0.1:8000/users/");
    }


  }
}

export default user;
