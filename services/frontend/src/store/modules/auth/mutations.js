export default {
  setUser(state, payload) {
    state.isLoggedIn = payload.isLoggedIn
    state.userName = payload.username
  }
}
