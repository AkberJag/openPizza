export default {
  // usage: context.commit('addToast', { toastTitle: "title", toastBody: "Body text" })
  // payload => {message: '', strongMessage: '', alertType: ''}
  addToast(state, payload) {
    payload.toastID = Date.now().toString()

    state.toasts.push(payload)
  },

  removeToast(state, payload) {
    state.toasts = state.toasts.filter((item) => item.toastID !== payload.idToRemove)
  },

  setTheme(state) {
    state.theme = state.theme === 'light' ? 'dark' : 'light'
    localStorage.setItem('theme', state.theme)
  }
}
