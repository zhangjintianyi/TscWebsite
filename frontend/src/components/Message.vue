<template>
    <div>
        <el-input class="search" placeholder="请输入搜索的标题或版本" icon="search" v-model="input"
        :on-icon-click="handleIconClick" @keyup.enter.native="handleIconClick">
        </el-input>
        <div v-if="!haveSearch" class="messages">
            <el-row v-for="(message, index)  in messages">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <span style="line-height: 36px; float:left;">版本：{{message.version}}</span>
                        <span style="line-height: 36px;">{{message.title}}</span>
                        <el-button style="float: right;" type="primary" @click="showMessageInfo(index)">更新</el-button>
                    </div>
                    <div>
                        <p>{{message.content}}</p>
                        <p class="time">{{message.add_time}}</p>
                    </div>
                </el-card>
            </el-row>
        </div>
        <div v-else class="messages">
            <el-row v-for="(message, index)  in filteredMessage">
                <el-card class="box-card">
                    <div slot="header" class="clearfix">
                        <span style="line-height: 36px; float:left;">版本：{{message.version}}</span>
                        <span style="line-height: 36px;">{{message.title}}</span>
                        <el-button style="float: right;" type="primary" @click="showMessageInfo(index)">更新</el-button>
                    </div>
                    <div>
                        <p>{{message.content}}</p>
                        <p class="time">{{message.add_time}}</p>
                    </div>
                </el-card>
            </el-row>
        </div>

    </div>
</template>

<script>
import instance from "@/api/fetch";

export default {
  name: "Message",
  data() {
    return {
      messages: [],
      input: "",
      filteredMessage: [],
      haveSearch: false
    };
  },
  methods: {
    getAllMessage() {
      instance.get("http://127.0.0.1:8000/messages/").then(rep => {
        const result = rep.data.results;
        console.log(rep.data.results);
        this.messages = result;
      });
    },
    showMessageInfo(index) {
      this.$store.dispatch("setMessage", this.messages[index]);
      this.$router.push("/message/info");
    },
    handleIconClick() {
      this.filteredMessage = [];
      let regex = new RegExp(this.input, "i");
      this.messages.forEach(message => {
        if (
          regex.test(message.title) ||
          regex.test(message.version) ||
          regex.test(message.content)
        ) {
          this.filteredMessage.push(message);
        }
      }, this);
      this.haveSearch = true;
      if (this.filteredMessage.length === 0 && this.haveSearch === true) {
        console.log("11111111");
        this.$notify.info({
          title: "麻烦看我一眼",
          message: "您貌似什么都没找到呦~~",
          duration: 1300
        });
      }
    }
  },
  created() {
    this.getAllMessage();
  },
  watch: {
    filteredMessage() {},
    input() {
      if (this.input === "") {
        this.haveSearch = false;
      }
    }
  }
};
</script>

<style scoped>
.box-card {
  width: 600px;
}

.text {
  font-size: 14px;
}

.time {
  font-size: 13px;
  color: #999;
}

.item {
  padding: 18px 0;
}

.el-row {
  margin-top: 20px;
  margin-bottom: 20px;
}
.search {
  width: 200px;
  margin-top: 15px;
}
.messages {
  text-align: center;
  margin-left: 500px;
}
</style>
