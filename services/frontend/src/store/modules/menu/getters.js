export default {
  getAllFoodCategories(state) {
    return state.menuCategories
  },
  getCategoryLoadingStatus(state) {
    return state.loadingMenuCategories
  },
  getLeftPaneComponent(state) {
    return state.leftPaneComponent
  },
  getRightPaneComponent(state) {
    return state.rightPaneComponent
  }
}
