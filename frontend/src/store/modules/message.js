import axios from "axios";
import instance from '@/api/fetch';

const message = {
  state: {
    id: null,
    writer: "",
    reminders: [],
    title: "",
    content: "",
    version: "",
    add_time: ""
  },
  getters: {
    id: state =>  state.id,
    email: state => state.email,
    reminders: state => state.reminders,
    title: state => state.title,
    content: state => state.content,
    version: state => state.version,
    add_time: state => state.add_time,
  },
  mutations: {
    SET_ID: (state, id) => {
      state.id = id;
    },
    SET_WRITER: (state, writer) => {
      state.writer = writer;
    },
    SET_REMINDERS: (state, reminders) => {
      state.reminders = reminders;
    },
    SET_TITLE: (state, title) => {
      state.title = title;
    },
    SET_CONTENT: (state, content) => {
      state.content = content;
    },
    SET_VERSION: (state, version) => {
      state.version = version;
    },
    SET_ADD_TIME: (state, add_time) => {
      state.add_time = add_time;
    },
  },
  actions: {
    setMessage({commit}, messageInfo) {
      commit("SET_ID", messageInfo.id);
      commit("SET_TITLE", messageInfo.title);
      commit("SET_CONTENT", messageInfo.content);
      commit("SET_VERSION", messageInfo.version);
      commit("SET_REMINDERS", messageInfo.reminders);
    },
    updateMessage({commit}, messageInfo) {
      console.log(messageInfo)
      let id = messageInfo.id;
      delete messageInfo.add_time; 
      instance.put("http://127.0.0.1:8000/messages/"+ id + "/", messageInfo)
      .then((response) => {
        console.log("resp", response.data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}

export default message;
