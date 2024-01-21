// a central API handler / customer fetch function
import store from './index.js'
const BASE_URL = 'http://localhost:5000'

async function apiRequest(endpoint, options) {
  const response = await fetch(`${BASE_URL}/${endpoint}`, options)
  if (response.status === 401) {
    // Handle unauthenticated response
    store.dispatch('auth/logout')
    return response
  }
  return response
}

export default apiRequest
