<template>
  <div
    class="toast"
    :class="newToastClass"
    role="alert"
    aria-live="assertive"
    aria-atomic="true"
    :id="id"
  >
    <div class="toast-header">
      <img class="rounded me-2" alt="🍕" :src="toastImgURL" />
      <strong class="me-auto">{{ toastTitle }}</strong>
      <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
    </div>
    <div class="toast-body">{{ toastBody }}</div>
  </div>
</template>

<script>
import { Toast } from 'bootstrap/dist/js/bootstrap.esm.min.js'
export default {
  props: ['id', 'toastTitle', 'toastBody', 'toastImgURL', 'toastClass'],
  data() {
    return {
      toast: null
    }
  },
  computed: {
    newToastClass() {
      let _toastClass = ''
      if (this.toastClass == 'success') {
        _toastClass = 'border-success'
      } else if (this.toastClass == 'danger') {
        _toastClass = 'border-danger'
      } else {
        _toastClass = ''
      }
      return _toastClass
    }
  },
  mounted() {
    this.toast = Toast.getOrCreateInstance('#' + this.id)
    this.toast.autohide = false
    this.toast.show()
    // console.log(this.$store.getters.getToasts)
    const myToastEl = document.getElementById(this.id)
    myToastEl.addEventListener('hidden.bs.toast', () => {
      this.$store.commit('removeToast', { idToRemove: this.id })
    })
  }
}
</script>
