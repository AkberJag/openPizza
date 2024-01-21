export default {
  async getAllFoodCategories(context) {
    try {
      // set the status to true so the loading spinner can be shown
      context.commit('menuCategoriesFetchingStatus', true)

      let url = 'http://localhost:5000/category/all'

      const response = await fetch(url, {
        method: 'GET',
        credentials: 'include'
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(response.statusText || 'Something went wrong')
      } else {
        const categories = []

        for (const key in responseData) {
          const category = {
            categoryID: responseData[key].id,
            categoryName: responseData[key].name
          }

          categories.push(category)
        }

        // add the fetched categories to the list
        context.commit('addMenuCategories', categories)
      }
    } catch (error) {
      console.error('Login error:', error)
      context.commit(
        'addToast',
        {
          toastTitle: 'Unable to fetch Categories',
          toastBody: error || 'Unable to fetch Categories',
          toastClass: 'danger'
        },
        { root: true }
      )
      context.commit('addMenuCategories', [-1])
    } finally {
      // set the status to false so the loading spinner can be removed
      context.commit('menuCategoriesFetchingStatus', false)
    }
  },

  async getAllItems(context, payload) {
    let url = `http://localhost:5000/category/${payload.itemID}`

    const response = await fetch(url, {
      method: 'GET',
      credentials: 'include'
    })

    const responseData = await response.json()

    if (responseData.items.length > 0) {
      context.commit('setItems', {
        data: responseData,
        itemArrayIndex: payload.itemArrayIndex
      })
    }
  }
}
