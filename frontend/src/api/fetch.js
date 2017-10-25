import axios from 'axios';
import Cookies from 'js-cookie';

import {
  BASE_URL
} from '@/environment';
import store from '@/store';

var instance = axios.create({
  baseURL: "http://192.168.69.110/api/v1/",
  timeout: 5000,
});

var csrftoken = Cookies.get("csrftoken")
axios.defaults.headers.common['X-CSRFToken'] = csrftoken;

instance.interceptors.request.use((config) => {
      if (store.getters.token) {
        config.headers['Authorization'] = "JWT " + store.getters.token;
      }
      return config;
    }, error => {
      // Do something with request error
      console.log(error); // for debug
      Promise.reject(error);
    })

export default instance;
