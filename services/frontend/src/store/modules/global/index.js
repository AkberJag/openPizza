import getters from './getters'
import mutations from './mutations'

export default {
  state() {
    return {
      toasts: [],
      theme: localStorage.getItem('theme') || 'light'
    }
  },
  getters,
  mutations
}
