<template>
    <div class="user-info">
        <el-upload class="avatar-uploader" :action="action" :headers="headers" :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
        <el-form ref="form" :model="form" label-width="100px">
            <el-form-item label="工号">
                <el-input v-model="form.jobNum"></el-input>
            </el-form-item>
            <el-form-item label="名字">
                <el-input v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item label="邮箱">
                <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="手机号">
                <el-input v-model="form.mobile"></el-input>
            </el-form-item>
            <el-form-item label="工位分机号">
                <el-input v-model="form.phone"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="saveUserInfo" :loading="loading">保存</el-button>
            </el-form-item>
        </el-form>

    </div>
</template>

<script>
import axios from 'axios';


export default {
    name: 'UserInfo',
    data() {
        return {
            imageUrl: "",
            action: "",
            loading: false,
            headers: {},
            form: {
                jobNum: "",
                username: "",
                email: "",
                mobile: "",
                phone: ""
            }
        }
    },
    methods: {
        handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
        },
        beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 / 1024 < 2;
            this.action = "http://127.0.0.1:8000/upload/avatar/" + file.name;
            if (this.$store.getters.token) {
                this.headers['Authorization'] = "JWT " + this.$store.getters.token;
            }
            if (!isJPG) {
                this.$message.error('上传头像图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
                this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
        },
        saveUserInfo() {
            this.loading = true;
            this.$store.dispatch("updateUserInfo", this.form)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/environment');
                })
                .catch((error) => {
                    this.$message.error(err);
                    this.loading = false;
                })
        },
        showUserInfo() {
            this.form.jobNum = this.$store.getters.jobNum;
            this.form.username = this.$store.getters.username;
            this.form.email = this.$store.getters.email;
            this.form.mobile = this.$store.getters.mobile;
            this.form.phone = this.$store.getters.phone;
        }
    },
    created () {
        this.$store.dispatch("getUserInfo", this.$store.getters.jobNum);
        this.showUserInfo();
    },
}
</script>

<style scoped>
.user-info {
    margin-top: 50px;
    margin-left: 200px;
    width: 500px;
}

.avatar-uploader .el-upload {
    border: 1px dashed #c9c9c9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.avatar-uploader .el-upload:hover {
    border-color: #20a0ff;
}

.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
}

.avatar {
    width: 178px;
    height: 178px;
    display: block;
}
</style>
