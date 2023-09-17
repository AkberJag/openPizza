<template>
  <router-view></router-view>
</template>

<script>
import { Popover } from 'bootstrap/dist/js/bootstrap.esm.min.js'
// import { Toast } from 'bootstrap/dist/js/bootstrap.esm.min.js'

export default {
  mounted() {
    // enable popover
    Array.from(document.querySelectorAll('button[data-bs-toggle="popover"]')).forEach(
      (popoverNode) => new Popover(popoverNode)
    )

    // //inti toast
    // Array.from(document.querySelectorAll('.toast')).forEach((toastNode) => new Toast(toastNode))
  }
}
</script>