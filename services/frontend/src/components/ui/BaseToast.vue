<template>
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" :id="id">
    <div class="toast-header">
      <img class="rounded me-2" alt="🍕" :src="toastImgURL" />
      <strong class="me-auto">{{ toastTitle }}</strong>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">{{ toastBody }}</div>
  </div>
</template>

<script>
import { Toast } from 'bootstrap/dist/js/bootstrap.esm.min.js'
export default {
  props: ['id', 'toastTitle', 'toastBody', 'toastImgURL'],
  data() {
    return {
      toast: null
    }
  },
  mounted() {
    this.toast = Toast.getOrCreateInstance('#' + this.id)
    this.toast.autohide = false
    setTimeout(() => {
      this.toast.show()
    }, 1000)
  },
  methods: {
    closeToast() {
      this.toast.hide()
    }
  }
}
</script>
