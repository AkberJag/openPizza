export default {
  // usage: this.$store.commit('addAlert', payload)
  // payload => {message: '', strongMessage: '', alertType: ''}
  addAlert(state, payload) {
    payload.id = Date.now()
    state.errors.push(payload)
  }
}
