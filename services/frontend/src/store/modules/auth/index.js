import actions from './actions'
import getters from './getters'
import mutations from './mutations'

export default {
  namespaced: true,
  state() {
    return {
      isLogginProcess: false,
      isLoggedIn: false,
      userName: ''
    }
  },
  actions,
  getters,
  mutations
}
