import actions from './actions'
import getters from './getters'

export default {
  namespaced: true,
  state() {
    return {
      isLoggedIn: false,
      userName: ''
    }
  },
  actions,
  getters
}
