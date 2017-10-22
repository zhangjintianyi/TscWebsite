<template>
    <div class="login-container">
        <!--todo: 登录表单验证-->
        <el-form autoComplete="on" :model="regForm" ref="regForm" label-position="left" label-width="0px" class="card-box login-form">
            <h3 class="title">注册</h3>
            <el-form-item prop="jobNum">
                <el-input name="jobNum" type="text" v-model="regForm.jobNum" autoComplete="on" placeholder="工号"></el-input>
            </el-form-item>
            <el-form-item prop="usrname">
                <el-input name="usrname" type="text" v-model="regForm.username" autoComplete="on" placeholder="名字"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input name="password" type="password" @keyup.enter.native="handleReg" v-model="regForm.password" autoComplete="on" placeholder="密码"></el-input>
            </el-form-item>
            <el-button type="primary" style="width:100%;" :loading="loading" @click.native.prevent="handleReg">
                注册
            </el-button>
            <div class='tips'>工号，型如:z18861</div>
            <div class='tips'>名字，请填写自己的真实姓名</div>
        </el-form>
    </div>
</template>

<script>
export default {
    name: "Reg",
    data() {
        return {
            regForm: {
                jobNum: "",
                username: "",
                password: ""
            },
            loading: false,
        }
    },
    methods: {
        handleReg() {
            this.loading = true;
            this.$store.dispatch('Reg', this.regForm)
                .then(() => {
                    this.loading = false;
                    this.$router.push('/environment')
                })
                .catch((error) => {
                    this.$message.error(err);
                    this.loading = false;
                })
        }
    }
}
</script>

<style scoped>
.tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 5px;
}

.login-container {
    background-color: #2d3a4b;
    position: relative;
    width: 100%;
    height: 100%;
}

.login-container .el-input {
    height: 47px;
    width: 85%;
}

.login-container .el-form {
    position: absolute;
    left: 0;
    right: 0;
    width: 400px;
    padding: 35px 35px 15px 35px;
    margin: 120px auto;
}

.el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
}

.el-button {
    margin-left: 0px;
    margin-bottom: 10px;
}

.title {
    font-size: 26px;
    font-weight: 400;
    color: #eeeeee;
    margin: 0px auto 40px auto;
    text-align: center;
}
</style>
