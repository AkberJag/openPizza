<template>
  <div>
    <TheAlertContainer />
    <TheToastContainer />
    <div class="container-fluid">
      <div class="row flex-nowrap no-gutters">
        <div v-if="true" class="col-auto p-0">
          <SideBar @themeChange="themeChange" />
        </div>
        <div class="col p-0">
          <div class="container-fluid vh-100" style="overflow: hidden">
            <router-view v-slot="{ Component }">
              <transition name="route" mode="out-in">
                <component :is="Component" />
              </transition>
            </router-view>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Popover } from 'bootstrap/dist/js/bootstrap.esm.min.js'

import TheAlertContainer from '@/components/layout/TheAlertContainer.vue'
import SideBar from '@/components/layout/TheSideBar.vue'
import TheToastContainer from './components/layout/TheToastContainer.vue'

export default {
  components: { TheAlertContainer, SideBar, TheToastContainer },
  mounted() {
    // Set app theme
    document.body.setAttribute('data-bs-theme', this.$store.getters.getTheme)
    // enable popover
    Array.from(document.querySelectorAll('button[data-bs-toggle="popover"]')).forEach(
      (popoverNode) => new Popover(popoverNode)
    )
  },
  methods: {
    themeChange(val) {
      document.body.setAttribute('data-bs-theme', val)
    }
  }
}
</script>

<style>
html,
body {
  height: 100%;
}

img {
  pointer-events: none;
}
.cursorPointer {
  cursor: pointer;
}
.route-leave-from,
.route-enter-to {
  opacity: 1;
}
.route-enter-from,
.route-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.route-enter-active {
  transition: all 0.3s ease-in;
}
.route-leave-active {
  transition: all 0.3s ease-out;
}
</style>
