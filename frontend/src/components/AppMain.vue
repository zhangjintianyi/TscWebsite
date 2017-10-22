<template>
    <div class="app-main">
        <el-row class="app-row">
            <el-col :span="4" class="navbar">
                <NavBar></NavBar>
            </el-col>
            <el-col :span="20">
                <router-view></router-view>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import NavBar from '@/components/Nav'

export default {
    name: "AppMain",
    data() {
        return {

        }
    },
    components: {
        NavBar,
    }
}
</script>

<style scoped>
.app-main {
    height: 100%;
}
.app-row {
    height: 100%;
}

.navbar {
    height: 100%;
}
</style>
