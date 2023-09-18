import router from '@/router/index.js'
export default {
  async login(context, payload) {
    let login_url = 'http://localhost:5000/api/v1/login'
    let body = new URLSearchParams({
      username: payload.email,
      password: payload.password
    })
    let headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

    const response = await fetch(login_url, {
      credentials: 'include',
      method: 'POST',
      headers,
      body
    })

    const responseData = await response.json()

    if (!response.ok) {
      const error = new Error(responseData.message || 'Failed to authenticate')
      throw error
    }

    if (responseData.access_token) {
      router.replace('/')
    }
  }
}
