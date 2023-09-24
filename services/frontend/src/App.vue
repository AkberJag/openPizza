<template>
  <div>
    <TheAlertContainer />
    <router-view v-slot="{ Component }">
      <transition name="route" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script>
import { Popover } from 'bootstrap/dist/js/bootstrap.esm.min.js'
// import { Toast } from 'bootstrap/dist/js/bootstrap.esm.min.js'
import TheAlertContainer from '@/components/layout/TheAlertContainer.vue'

export default {
  components: { TheAlertContainer },
  mounted() {
    // Set app theme
    document.body.setAttribute('data-bs-theme', 'light')
    // enable popover
    Array.from(document.querySelectorAll('button[data-bs-toggle="popover"]')).forEach(
      (popoverNode) => new Popover(popoverNode)
    )
    //inti toast
    // Array.from(document.querySelectorAll('.toast')).forEach((toastNode) => new Toast(toastNode))
  }
}
</script>

<style>
html,
body {
  height: 100%;
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
