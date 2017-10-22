<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/Nav'
import LabEnvTable from '@/components/LabEnvTable';
export default {
  name: 'app',
  components: {
    NavBar, LabEnvTable
  }
}
</script>

<style>
#app {
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.app-row {
  height: 100%;
}

.navbar {
  height: 100%;
}
</style>
