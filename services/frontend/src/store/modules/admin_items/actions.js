import apiRequest from '../../api.js'

export default {
  async createCategory(context, payload) {
    let endpoint = 'category'

    try {
      let body = JSON.stringify({ name: payload.name })

      let headers = { 'Content-Type': 'application/json' }

      const response = await apiRequest(endpoint, {
        method: 'POST',
        headers,
        body
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(responseData.detail || 'Failed to add category')
      } else {
        context.commit(
          'addToast',
          {
            toastTitle: 'Category added',
            toastBody: `${payload.name} added`,
            toastClass: 'success'
          },
          { root: true }
        )
      }
    } catch (error) {
      context.commit(
        'addToast',
        {
          toastTitle: 'Something went wrong',
          toastBody: error.message || 'Unknown error',
          toastClass: 'danger'
        },
        { root: true }
      )
    }
  },

  async createItem(context, payload) {
    let endpoint = 'items'

    try {
      let body = JSON.stringify({
        name: payload.name,
        price: payload.price,
        description: payload.description,
        category_id: payload.category_id
      })

      let headers = { 'Content-Type': 'application/json' }

      const response = await apiRequest(endpoint, {
        method: 'POST',
        headers,
        body
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(responseData.detail || 'Failed to add item')
      } else {
        context.commit(
          'addToast',
          {
            toastTitle: 'Item added',
            toastBody: `${payload.name} added into ${payload.category_name}`,
            toastClass: 'success'
          },
          { root: true }
        )
      }
    } catch (error) {
      context.commit(
        'addToast',
        {
          toastTitle: 'Something went wrong',
          toastBody: error.message || 'Unknown error',
          toastClass: 'danger'
        },
        { root: true }
      )
    }
  }
}
