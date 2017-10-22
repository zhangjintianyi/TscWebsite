<template>
    <div class="nav" mode="horizontal">
        <el-menu theme="dark" class="nav-menu">
            <el-menu-item index="1" @click="enterMyInfo">
                <img :src="avatar" alt="头像" height="50" width="50">
                <p>{{this.$store.getters.jobNum}}</p>
            </el-menu-item>
            <el-menu-item index="2" @click="showEnv">实验室环境</el-menu-item>
            <el-menu-item index="3" @click="showDoc">TSC文档</el-menu-item>
            <el-menu-item index="4" @click="showTopo">拓扑</el-menu-item>
            <el-menu-item index="5" @click="showMessage">消息</el-menu-item>
        </el-menu>
    </div>
</template>

<script>
export default {
    name: "Nav",
    data() {
        return {
            avatar: "../../static/avatar.png"
        }
    },
    methods: {
        showEnv() {
            this.$router.push("/")
        },
        showDoc() {
            this.$router.push("/doc")
        },
        showTopo() {
            this.$router.push("/topo")
        },
        showMessage() {
            this.$router.push("/message")
        },
        enterMyInfo() {
            this.$router.push("/user")
        }
    },
    watch: {
        avatar() {
            return this.$store.getters.avatar;
        }
    }

}
</script>

<style scoped>
.nav {
    height: 100%;
}

.nav-menu {
    height: 100%;
}

img {
    border-radius: 25px;
    border: 1px solid;
    margin-bottom: -10px;
}
.el-menu-item {
    margin-bottom: 50px;
}
</style>
