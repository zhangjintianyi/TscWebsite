<template>
  <div>
    <!--实验室环境展示开关-->
    <div class="switch">
      <p>简单展示</p>
      <el-switch v-model="switchOn" on-color="#13ce66" off-color="#C3C3C3" n-value="true" off-value="false" @change="simpleSwitchOff">
      </el-switch>
    </div>

    <!--实验室环境简单展示-->
    <div class="env-tree">
      <el-tree :data="mso_tsc_info" @node-click="handleNodeClick"></el-tree>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LabEnv',
  data() {
    return {
      switchOn: true,
      mso_tsc_info: [],
    }
  },

  methods: {
    _loadTreeData(rawData) {
      for (let i = 0; i < rawData.length; i++) {
        let mso = {}, tsc = [];
        mso["label"] = "MSO: " + rawData[i].ip;
        if (rawData[i].have_tsc) {
          for (let j = 0; j < rawData[i].have_tsc.length; j++) {
            let oneTSC = {};
            oneTSC["label"] = "TSC: " + rawData[i].have_tsc[j]["ip"]
            tsc.push(oneTSC);
          }
          console.log("tsc", tsc)
        }
        mso["children"] = tsc;
        this.mso_tsc_info.push(mso);
      }
    },

    _getMSOTSCInfo() {
      axios.get("http://192.168.69.110/api/v1/mso/")
        .then(res => {
          this._loadTreeData(res.data.results)
        })
        .catch(error => {
          console.log(error)
        })
    },

    handleNodeClick(data) {
      console.log(data.$treeNodeId)
    },

    simpleSwitchOff() {
      this.$store.dispatch('ToggleSimpleSwitch');
      this.$router.push("/")
    }
  },

  created() {
    this._getMSOTSCInfo();
  },


}
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.switch {
  position: relative;
  top: 10px;
  left: 40%;
}

.env-tree {
  margin-top: 3%;
}
</style>
