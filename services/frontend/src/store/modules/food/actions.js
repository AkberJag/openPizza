export default {
  async getAllFoodCategories(context) {
    let url = 'http://localhost:5000/api/v1/home/food_categories'

    const response = await fetch(url, {
      method: 'GET',
      credentials: 'include'
    })

    const responseData = await response.json()

    const categories = []
    for (const key in responseData) {
      const category = {
        categoryID: responseData[key].category_id,
        categoryName: responseData[key].category_name,
        categoryImageURL: responseData[key].category_image_url
      }
      categories.push(category)
    }
    context.commit('addCategory', categories)
  },
  async getAllItems(context, payload) {
    let url = `http://localhost:5000/api/v1/home/food_category/${payload}/food_items`

    const response = await fetch(url, {
      method: 'GET',
      credentials: 'include'
    })

    const responseData = await response.json()
    context.commit('setItems', { id: payload, data: responseData })
  }
}
