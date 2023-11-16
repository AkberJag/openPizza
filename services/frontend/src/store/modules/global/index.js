import mutations from './mutations'
import getters from './getters'

export default {
  state() {
    return {
      errors: [{ message: 'test', strongMessage: 'St' }],
      toasts: [{ toastTitle: 'Test toast', toastBody: 'This is a test toast' }],
      theme: localStorage.getItem('theme') || 'light'
    }
  },
  mutations,
  getters
}
