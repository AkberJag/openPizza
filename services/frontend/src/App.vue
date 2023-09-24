<template>
  <div>
    <TheAlertContainer />
    <router-view></router-view>
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
