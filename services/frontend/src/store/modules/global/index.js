import actions from './actions'
import mutations from './mutations'

export default {
  state() {
    return {
      errors: []
    }
  },
  actions,
  mutations
}
