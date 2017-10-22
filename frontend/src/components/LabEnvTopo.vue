<template>
    <div>
        <div v-if="dialogMSOVisible">
            <el-dialog :title="'Mso: '+info.ip" :visible.sync="dialogMSOVisible" size="tiny" :before-close="handleClose">
                <p>中控id：
                    <span>{{info.mso_id}}</span>
                </p>
                <p>设备归属部门：
                    <span>{{info.department}}</span>
                </p>
                <p>交换机连接端口：
                    <span>{{info.port}}</span>
                </p>
                <p>型号及其他：
                    <span>{{info.unit_type}}</span>
                </p>
                <p>使用版本：
                    <span>{{info.version}}</span>
                </p>
                <p>搭建时间：
                    <span>{{info.setup_time}}</span>
                </p>
                <p>环境负责人：
                    <span>{{info.principal}}</span>
                </p>
            </el-dialog>
        </div>
        <div v-if="dialogTSCVisible">
            <el-dialog :title="'TSC: '+current_tsc.ip" :visible.sync="dialogTSCVisible" size="tiny" :before-close="handleClose">
                <p>中控id：
                    <span>{{current_tsc.tsc_id}}</span>
                </p>
                <p>设备归属部门：
                    <span>{{current_tsc.department}}</span>
                </p>
                <p>交换机连接端口：
                    <span>{{current_tsc.port}}</span>
                </p>
                <p>型号及其他：
                    <span>{{current_tsc.unit_type}}</span>
                </p>
                <p>载频数：
                    <span>{{current_tsc.carrier_num}}</span>
                </p>
                <p>使用版本：
                    <span>{{current_tsc.version}}</span>
                </p>
                <p>搭建时间：
                    <span>{{current_tsc.setup_time}}</span>
                </p>
                <p>环境负责人：
                    <span>{{current_tsc.principal}}</span>
                </p>
            </el-dialog>
        </div>
        <canvas id="canvas" :height="canvasHeight" :width="canvasWidth" class="canvas">
        </canvas>
    </div>
</template>

<script>
export default {
    name: "TOPO",
    props: ['info'],
    data() {
        return {
            tsc_pos: [],
            current_tsc: {},
            dialogMSOVisible: false,
            dialogTSCVisible: false,
            mso_x: window.innerWidth / 3,
            mso_y: window.innerHeight / 2,
        }
    },
    computed: {
        canvasHeight() {
            return window.innerHeight;
        },
        canvasWidth() {
            return window.innerWidth * 5 / 6;
        }
    },
    methods: {
        handleClose() {
            this.dialogMSOVisible = false;
            this.dialogTSCVisible = false;
        },
        _isClickMso(position) {
            return (position.x >= this.mso_x && position.x <= this.mso_x + 50
                && position.y >= this.mso_y && position.y <= this.mso_y + 50);
        },
        _isClickTsc(pos) {
            console.log("tsc_pos", this.tsc_pos[0])
            if (pos.x >= this.tsc_pos[0].x && pos.x <= this.tsc_pos[0].x + 50
                && pos.y >= this.tsc_pos[0].y && pos.y <= this.tsc_pos[0].y + 50) {
                this.current_tsc = this.info.have_tsc[0];
                return this.current_tsc;
            } else if (pos.x >= this.tsc_pos[1].x && pos.x <= this.tsc_pos[1].x + 50
                && pos.y >= this.tsc_pos[1].y && pos.y <= this.tsc_pos[1].y + 50) {
                this.current_tsc = this.info.have_tsc[1];
                return this.current_tsc;
            } else if (pos.x >= this.tsc_pos[2].x && pos.x <= this.tsc_pos[2].x + 50
                && pos.y >= this.tsc_pos[2].y && pos.y <= this.tsc_pos[2].y + 50) {
                this.current_tsc = this.info.have_tsc[2];
                return this.current_tsc;
            }
        },
        _showInfo(event) {
            let p = this._getEventPosition(event);
            console.log(p)
            if (this._isClickMso(p)) {
                this.dialogMSOVisible = true;
            }
            if (this._isClickTsc(p)) {
                this.dialogTSCVisible = true;
            }
        },
        _getEventPosition(ev) {
            let x, y;
            if (ev.layerX || ev.layerY) {
                x = ev.layerX;
                y = ev.layerY;
            } else if (ev.offsetX || ev.offsetY) {
                x = ev.offsetX;
                y = ev.offsetY;
            }

            return { x: x, y: y }
        },
        _drawTopo(ctx) {
            //画中控
            let imageMso = new Image();
            const LINE = 200, IMAGE_SIZE = 50;
            imageMso.onload = () => {
                console.log(IMAGE_SIZE)
                ctx.drawImage(imageMso, this.mso_x, this.mso_y, IMAGE_SIZE, IMAGE_SIZE);
            }
            imageMso.id = "msoImg";
            imageMso.src = "../../static/mso.png";
            console.log(imageMso)

            //画基站
            let imageTsc = new Image();
            imageTsc.onload = () => {
                let info = this.info;
                let angle_once = Math.PI * 2 / info.have_tsc.length;
                let angle = 0;
                for (let i = 0; i < info.have_tsc.length; i++) {
                    let tsc_x = this.mso_x + LINE * Math.cos(angle);
                    let tsc_y = this.mso_y - LINE * Math.sin(angle);
                    this.tsc_pos.push({ x: tsc_x, y: tsc_y });
                    ctx.drawImage(imageTsc, tsc_x, tsc_y, IMAGE_SIZE, IMAGE_SIZE);
                    angle = angle + angle_once;
                    //画连接线
                    ctx.beginPath();
                    ctx.moveTo(this.mso_x + IMAGE_SIZE / 2, this.mso_y + IMAGE_SIZE / 2);
                    ctx.lineTo(tsc_x + IMAGE_SIZE / 2, tsc_y + IMAGE_SIZE / 2);
                    ctx.stroke();
                }
            }
            imageTsc.src = "../../static/tsc.png";

        },
        _draw() {
            let canvas = document.getElementById("canvas");
            canvas.addEventListener("dblclick", (event) => {
                this._showInfo(event);
            });
            console.log("canvas----", canvas)
            if (canvas.getContext) {
                let ctx = canvas.getContext('2d');
                canvas.height = canvas.height;
                this._drawTopo(ctx);
            } else {
                console.log("你的浏览器不支持canvas，请升级浏览器");
            }

        }
    },
    watch: {
        info() {
            this._draw();
        }
    },
}
</script>

<style scoped>

</style>
