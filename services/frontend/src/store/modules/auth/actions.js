import router from '@/router/index.js'
import { BASE_URL } from '../../api.js'
import apiRequest from '../../api.js'

export default {
  async login(context, payload) {
    try {
      context.commit('setLoginInStatus', { val: true })
      const endpoint = 'login'
      const body = new URLSearchParams({
        username: payload.email,
        password: payload.password
      })
      const headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

      const response = await fetch(`${BASE_URL}/${endpoint}`, {
        credentials: 'include',
        method: 'POST',
        headers,
        body
      })

      const responseData = await response.json()

      if (!response.ok) {
        throw new Error(responseData.detail || 'Failed to authenticate')
      }

      if (responseData.is_active) {
        context.commit('setUser', { isLoggedIn: true, username: responseData.name })
        context.commit(
          'addToast',
          {
            toastTitle: 'Welcome',
            toastBody: `Hi ${responseData.name}, Login successful.`,
            toastClass: 'success'
          },
          { root: true }
        )
        router.replace({ name: 'MenuRoute' })
      }
    } catch (error) {
      console.error('Login error:', error)
      context.commit(
        'addToast',
        {
          toastTitle: 'Something went wrong',
          toastBody: error.message || 'Unknown error',
          toastClass: 'danger'
        },
        { root: true }
      )
    } finally {
      context.commit('setLoginInStatus', { val: false })
    }
  },

  async register(context, payload) {
    try {
      context.commit('setLoginInStatus', { val: true })

      const endpoint = 'user'

      const body = JSON.stringify({
        name: payload.fullname,
        email: payload.email,
        password: payload.password
      })

      const headers = { 'Content-Type': 'application/json' }

      const response = await apiRequest(endpoint, {
        method: 'POST',
        headers,
        body
      })

      const responseData = await response.json()

      if (!response.ok) {
        let error_message = ''
        if (typeof responseData.detail === 'object') {
          error_message = `${responseData.detail[0].loc[1] || ''} ${responseData.detail[0].msg}`
        } else {
          error_message = responseData.detail
        }
        throw new Error(error_message || 'Registration failed')
      } else if (responseData) {
        context.commit(
          'addToast',
          {
            toastTitle: 'Success',
            toastBody: `Registration complete, Please login now.`,
            toastClass: 'success'
          },
          { root: true }
        )
        router.replace({ name: 'LoginRoute' })
      }
    } catch (error) {
      context.commit(
        'addToast',
        {
          toastTitle: 'Registration failed',
          toastBody: error.message || 'Unknown error',
          toastClass: 'danger'
        },
        { root: true }
      )
    } finally {
      context.commit('setLoginInStatus', { val: false })
    }
  },

  async logout(context) {
    let logout_endpoint = 'user/logout'
    await apiRequest(logout_endpoint, { credentials: 'include', method: 'GET' })
    context.commit('setUser', { isLoggedIn: false })
    router.replace({ name: 'LoginRoute' })
  },

  async try_auto_login(context) {
    // Auto Login using the stored cookie
    let endpoint = 'user/me'

    try {
      const response = await apiRequest(endpoint, { method: 'GET', credentials: 'include' })
      const responseData = await response.json()
      if (responseData.is_active === true && response.ok) {
        context.commit('setUser', { isLoggedIn: true, username: responseData.name })
      }
    } catch (error) {
      console.error('error:', error)
    }
  }
}
