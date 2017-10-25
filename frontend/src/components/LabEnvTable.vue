<template>
    <div>
        <!--实验室环境展示开关-->
        <div class="switch">
            <p>简单展示</p>
            <el-switch v-model="switchOn" on-color="#13ce66" off-color="#C3C3C3" n-value="true" off-value="false" @change="simpleSwitchOn">
            </el-switch>
        </div>

        <!--实验室环境表格展示-->
        <div class="env-table">
            <ul>
                <li v-for="msoData in tableData">
                    <div class="mso">
                        <el-popover ref="popover1" placement="right" :title="'IP: '+ msoData[0].ip" width="200" trigger="click"
                        :content="'版本： '+msoData[0].version + ' '+ '负责人： '+msoData[0].principal">
                            <el-button slot="reference" class="mso-btn">MSO: {{msoData[0].ip}}</el-button>
                        </el-popover>
                    </div>

                    <el-table :data="msoData[0].have_tsc" style="width: 100%">
                        <el-table-column type="expand">
                            <template scope="props">
                                <el-form label-position="left" inline class="demo-table-expand">
                                    <el-form-item label="TSC ID">
                                        <span>{{ props.row.id }}</span>
                                    </el-form-item>
                                    <el-form-item label="TSC IP">
                                        <span>{{ props.row.ip }}</span>
                                    </el-form-item>
                                    <el-form-item label="所属部门">
                                        <span>{{ props.row.department }}</span>
                                    </el-form-item>
                                    <el-form-item label="端口">
                                        <span>{{ props.row.port }}</span>
                                    </el-form-item>
                                    <el-form-item label="载频数">
                                        <span>{{ props.row.carrier_num }}</span>
                                    </el-form-item>
                                    <el-form-item label="设备类型">
                                        <span>{{ props.row.unit_type }}</span>
                                    </el-form-item>
                                    <el-form-item label="TSC版本">
                                        <span>{{ props.row.version }}</span>
                                    </el-form-item>
                                    <el-form-item label="搭建时间">
                                        <span>{{ props.row.setup_time }}</span>
                                    </el-form-item>
                                    <el-form-item label="集群类型">
                                        <span>{{ props.row.tsc_type }}</span>
                                    </el-form-item>
                                    <el-form-item label="负责人">
                                        <span>{{ props.row.principal }}</span>
                                    </el-form-item>
                                </el-form>
                            </template>
                        </el-table-column>
                        <el-table-column label="TSC ID" prop="id">
                        </el-table-column>
                        <el-table-column label="TSC IP" prop="ip">
                        </el-table-column>
                        <el-table-column label="TSC版本" prop="version">
                        </el-table-column>
                        <el-table-column label="负责人" prop="principal">
                        </el-table-column>
                    </el-table>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "LabEnvTable",
    data() {
        return {
            switchOn: false,
            tableData: [],
            msoIP: null,
        }
    },
    methods: {
        _getChangeInfo(data) {
            for (var index = 0; index < data.length; index++) {
                if (data[index].tsc_type === 1) {
                    data[index].tsc_type = "大集群";
                } else {
                    data[index].tsc_type = "小集群";
                }
            }
        },
        _getEnvInfo() {
            axios.get("http://192.168.69.110/api/v1/mso/")
                .then(res => {
                    let tableData = [];
                    res.data.results.forEach(function(element) {
                        tableData.push([element]);
                    }, this);
                    this.tableData = tableData;
                    console.log("results", this.tableData);
                    for (let index = 0; index < this.tableData.length; index++) {
                        this.msoIP = this.tableData[index][0].ip;
                        this._getChangeInfo(this.tableData[index][0].have_tsc);
                        console.log(this.tableData[index][0].have_tsc)
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        },
        simpleSwitchOn() {
            this.$store.dispatch('ToggleSimpleSwitch');
            this.$router.push("/environment/simple")
        }
    },
    created() {
        this._getEnvInfo();
    }
}
</script>

<style scoped>
.demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
}

.switch {
    position: relative;
    top: 10px;
    left: 40%;
}

.env-table {
    margin-top: 3%;
}
.mso {
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 20px;
    text-align: left;
}
.mso-btn {
    border: none;
}
</style>
