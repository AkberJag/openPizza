import mutations from './mutations'
import getters from './getters'

export default {
  state() {
    return {
      errors: [{ message: 'test', strongMessage: 'St' }],
      theme: 'light'
    }
  },
  mutations,
  getters
}
