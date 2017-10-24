<template>
    <div>
        <div class="btn-group">
            <el-button class="btn-back" type="primary" @click="back">上一个系统</el-button>
            <el-button class="btn-forword" type="primary" @click="forword">下一个系统</el-button>
        </div>
        <div>
            <Topo :info="currentInfo"></Topo>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Topo from '@/components/LabEnvTopo';

export default {
    name: "EnvTopo",
    components: {
        Topo
    },
    data() {
        return {
            info_list: [],
            currentInfo: {},
            currentIndex: 0,
        }
    },
    methods: {
        _getMSOTSCInfo() {
            axios.get("http://localhost:8000/api/v1/mso")
                .then(res => {
                    this.info_list = res.data.results;
                    this.currentInfo = this.info_list[0];
                    this.currentIndex = 0;
                    console.log(this.info_list);
                })
                .catch(error => {
                    console.log(error)
                })
        },
        back() {
            if (this.currentIndex > 0 && this.currentIndex < this.info_list.length) {
                --this.currentIndex;
                this.currentInfo = this.info_list[this.currentIndex];
            }
        },
        forword() {
            if (this.currentIndex >= 0 && this.currentIndex < this.info_list.length - 1) {
                ++this.currentIndex;
                this.currentInfo = this.info_list[this.currentIndex];
            }
        }
    },
    created() {
        this._getMSOTSCInfo();
    }
}
</script>

<style scoped>
img {
    height: 50px;
    width: 50px;
}

.btn-group {
    margin-top: 10px;
    height: 50px;
}

.btn-back {
    margin-right: 10px;
}
</style>
