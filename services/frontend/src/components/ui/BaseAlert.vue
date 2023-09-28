<template>
  <div
    class="alert alert-dismissible fade show mb-2 shadow-sm"
    role="alert"
    :class="'alert-' + alertType"
    :id="alertID"
  >
    <i class="bi bi-exclamation-triangle-fill me-2"></i>
    <strong v-if="strongMessage">{{ strongMessage }}</strong> {{ message }} {{ alertID }}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
</template>

<script>
import { Alert } from 'bootstrap/dist/js/bootstrap.esm.min.js'
export default {
  props: {
    alertType: {
      type: String,
      default: 'warning'
    },
    alertID: String,
    message: String,
    strongMessage: String
  },
  data() {
    return {
      closeTimer: null
    }
  },
  methods: {
    clearCloseTimeout() {
      clearTimeout(this.closeTimer)
    }
  },
  mounted() {
    const alert = Alert.getOrCreateInstance('#' + this.alertID)
    this.closeTimer = setTimeout(() => {
      alert.close()
    }, 10000)
  }
}
</script>
