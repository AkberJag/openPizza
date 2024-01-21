export default {
  setUser(state, payload) {
    state.isLoggedIn = payload.isLoggedIn
    state.userName = payload.username
  },
  setLoginInStatus(state, payload) {
    state.isLogginProcess = payload.val
  }
}
