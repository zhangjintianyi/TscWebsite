<template>
    <div class="message-publish">
        <el-form ref="form" :model="form" label-width="100px">
            <el-form-item label="标题" placeholder="请输入标题">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="内容" placeholder="请输入内容">
                <el-input type="textarea" :autosize="{ minRows: 6, maxRows: 10 }" v-model="form.content"></el-input>
            </el-form-item>
            <el-form-item label="版本" placeholder="请输入版本">
                <el-input v-model="form.version"></el-input>
            </el-form-item>
            <el-form-item label="提醒人">
                <!--<el-select v-model="value" placeholder="请选择提醒人">
                                                                        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                                                                        </el-option>
                                                                    </el-select>-->
                <!--<el-transfer filterable filter-placeholder="请输入提醒人" v-model="value" :data="data" class="transfer">
                                                    </el-transfer>-->
                <Transfer :data="data" :target-keys="targetKeys" filterable @on-change="handleChange" :titles="titles" :filter-placeholder="placeHolder"></Transfer>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="publishMessage">发布消息</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import instance from '@/api/fetch';

export default {
    name: "MessagePublish",
    data() {
        return {
            form: {
                id: "",
                writer: "",
                title: "",
                content: "",
                version: "",
                add_time: "",
                reminders: []
            },
            data: [],
            targetKeys: [],
            titles: ["组内小伙伴", "选中的孩子"],
            placeHolder: "请输入提醒人"
        }
    },
    methods: {
        handleChange(newTargetKeys) {
            this.targetKeys = newTargetKeys;
            this.form.reminders = this.targetKeys;
        },
        formatOptions(data) {
            data.forEach(function(element) {
                let option = {}
                option["key"] = element.job_num;
                option["label"] = !element.username ? element.job_num : element.username;
                this.data.push(option)
            }, this);
        },
        getAllUserInfo() {
            this.$store.dispatch("getAllUserInfo")
                .then(response => {
                    console.log(response.data)
                    this.formatOptions(response.data);
                })
        },
        publishMessage() {
            this.form.writer = this.$store.getters.jobNum;
            instance.post("http://127.0.0.1:8000/messages/", this.form);
            this.$router.push("/message");
        }
    },
    created() {
        this.getAllUserInfo();
    }
}
</script>

<style scoped>
.message-publish {
    margin-top: 50px;
    margin-left: 200px;
    width: 600px;
}
</style>
