export default {
  isAuthenticated(state) {
    return state.isLoggedIn
  },
  getuserName(state) {
    return state.userName
  },
  getLoginInStatus(state) {
    return state.isLogginProcess
  },
}
