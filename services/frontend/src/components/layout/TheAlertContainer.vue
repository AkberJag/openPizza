<template>
  <div class="container text-center my-1" style="max-height: 150px; overflow-y: auto">
    <base-alert
      v-for="(alert, index) in alerts"
      :key="index"
      :alertID="alert.id.toString()"
      :message="alert.message"
      :strongMessage="alert.strongMessage"
    ></base-alert>
  </div>
</template>

<script>
import BaseAlert from '@/components/ui/BaseAlert.vue'
export default {
  components: { BaseAlert },

  data() {
    return {
      alerts: this.$store.state.global.errors
    }
  }
}
</script>

<style scoped>
.container {
  position: absolute;
  z-index: 2000;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
}
</style>
