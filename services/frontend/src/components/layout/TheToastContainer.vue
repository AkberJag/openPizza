<template>
  <div class="toast-container position-fixed bottom-0 end-0 p-2">
    <BaseToast
      v-for="(toast, index) in toasts"
      :key="index"
      :id="Date.now().toString()"
      :toastTitle="toast.toastTitle"
      :toastBody="toast.toastBody"
      :toastImgURL="toast.toastImgURL"
    />
  </div>
</template>

<script>
import BaseToast from '@/components/ui/BaseToast.vue'
export default {
  components: { BaseToast },

  data() {
    return {
      toasts: this.$store.state.global.toasts
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
