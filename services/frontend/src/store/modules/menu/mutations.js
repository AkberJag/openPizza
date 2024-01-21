export default {
  addMenuCategories(state, payload) {
    state.menuCategories = payload
  },
  menuCategoriesFetchingStatus(state, payload) {
    state.loadingMenuCategories = payload
  },
  setItems(state, payload) {
    state.menuCategories[payload.itemArrayIndex].items = payload.data.items
  },
  setLeftPaneComponent(state, payload) {
    state.leftPaneComponent = payload
  },
  setRightPaneComponent(state, payload) {
    state.rightPaneComponent = payload
  }
}
