<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-3 v-100">
    <BaseToast
      v-for="(toast, index) in toasts"
      :key="index"
      :id="toast.toastID"
      :toastTitle="toast.toastTitle"
      :toastBody="toast.toastBody"
      :toastImgURL="toast.toastImgURL"
      :toastClass="toast.toastClass"
    />
  </div>
</template>

<script>
import BaseToast from '../../components/ui/TheBaseToast.vue'
export default {
  components: { BaseToast },

  computed: {
    toasts() {
      return this.$store.getters.getToasts
    }
  }
}
</script>

<style scoped>
.toast-container {
  max-height: 500px;
  overflow: auto;
}
</style>
