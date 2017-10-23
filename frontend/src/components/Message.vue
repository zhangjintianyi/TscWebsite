<template>
  <div>
    <el-input class="search" placeholder="请输入搜索的标题或版本" icon="search" v-model="input" :on-icon-click="handleIconClick" @keyup.enter.native="handleIconClick">
    </el-input>
    <el-button type="primary" @click="publishMessage">发布消息</el-button>
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
    <div v-if="!haveSearch" class="block">
      <el-pagination @current-change="handleCurrentChange" :page-size="5" layout="prev, pager, next, jumper" :total="count">
      </el-pagination>
    </div>
    <div v-else-if="haveSearch && filteredMessage.length" class="block">
      <el-pagination @current-change="handleCurrentChange" :page-size="5" layout="prev, pager, next, jumper" :total="filteredMessage.length">
      </el-pagination>
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
      haveSearch: false,
      currentPage: 1,
      count: null,
      last100Messages: [],
    };
  },
  methods: {
    getCurrentPageMessage() {
      instance.get("http://127.0.0.1:8000/messages/?page=" + this.currentPage).then(rep => {
        const result = rep.data.results;
        this.count = rep.data.count;
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
      this.last100Messages.forEach(message => {
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
    },
    handleCurrentChange(currentPage) {
      console.log(`当前页: ${currentPage}`);
      this.currentPage = currentPage;
    },
    getLast100Messages() {
      let page = 1;
      console.log(this.count)
      let pageCount = this.count / 5;
      console.log("pageCount", pageCount)
      while (page <= 20) {
        instance.get("http://127.0.0.1:8000/messages/?page=" + page).then(rep => {
          this.last100Messages.push(...rep.data.results);
        });
        page++;
      }
    },
    publishMessage() {
      this.$router.push("/message/publish")
    }
  },
  mounted() {
    this.getCurrentPageMessage();
    this.getLast100Messages();
  },
  watch: {
    filteredMessage() { },
    input() {
      if (this.input === "") {
        this.haveSearch = false;
      }
    },
    currentPage() {
      this.getCurrentPageMessage();
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

.el-button {
  float: right;
  margin-top: 15px;
  margin-right: 15px;
}
</style>
