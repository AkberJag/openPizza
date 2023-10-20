export default {
  getAllFoodCategories(state) {
    const categoryInfo = state.menuData.map((category) => ({
      categoryID: category.categoryID,
      categoryName: category.categoryName,
      categoryImageURL: category.categoryImageURL
    }))

    return categoryInfo
  }
}
