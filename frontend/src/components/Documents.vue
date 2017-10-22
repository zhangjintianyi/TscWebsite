<template>
  <div class="doc">
    <pdf src="../../static/Python.pdf" ref="pdf" :page="1" @numPages="numPages = $event" class="doc"></pdf>
    <!--<iframe src="../../static/Python.pdf" frameborder="0" scrolling="no" :height="pdfHeight" :width="pdfWidth"></iframe>-->
  </div>
</template>

<script>
import pdf from 'vue-pdf'
export default {
  name: 'Document',
  data() {
    return {
      numPages: 0
    }
  },
  components: {
    pdf
  },
  computed: {
    pdfHeight() {
      return document.body.scrollHeight;
    },
    pdfWidth() {
      return window.innerWidth * 5 / 6;
    }
  },
  methods: {
    resizeCanvas() {
      var canvas = document.getElementsByTagName("canvas");
      console.log('canvas', canvas);
      // w = canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    },
    resizeCanvasListener() {
      window.addEventListener("resize", this.resizeCanvas, false);
    },
  },
  mounted() {
    //this.resizeCanvasListener();
  }
}
</script>

<style scoped>
.doc {
  width: 100%;
  height: 100%;
}
</style>
