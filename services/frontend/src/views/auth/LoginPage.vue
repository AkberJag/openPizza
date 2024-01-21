<template>
  <div class="bg-body-tertiary h-100 w-100 body overflow-auto">
    <main class="form-signin w-100 m-auto">
      <div class="centered-container">
        <form class="centered-form" @submit.prevent="submitForm">
          <p class="user-select-none" style="font-size: 8cap">🍕</p>
          <h1 class="h3 mb-3 fw-normal">Please Login</h1>

          <div class="form-floating">
            <input
              type="email"
              class="form-control"
              id="floatingInput"
              placeholder="name@example.com"
              v-model.trim="email"
            />
            <label for="floatingInput">Email address / User Name</label>
          </div>
          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="Password"
              v-model.trim="password"
            />
            <label for="floatingPassword">Password</label>
          </div>

          <div class="form-check text-start my-3">
            <input
              class="form-check-input"
              type="checkbox"
              value="remember-me"
              id="flexCheckDefault"
            />
            <label class="form-check-label" for="flexCheckDefault">Remember me </label>
          </div>
          <button
            class="btn btn-primary w-100 py-2"
            :class="{ disabled: isLoggingIn }"
            type="submit"
          >
            <div v-if="!isLoggingIn">Log in</div>
            <BaseSpinner v-else class="text-light" style="width: 1.2rem; height: 1.2rem" />
          </button>

          <router-link
            :to="{ name: 'RegisterRoute' }"
            class="disabled link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover mt-3"
            :class="{ 'router-link-disabled': isLoggingIn }"
          >
            or Register
          </router-link>
        </form>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async submitForm() {
      await this.$store.dispatch('auth/login', { email: this.email, password: this.password })
    }
  },
  computed: {
    isLoggingIn() {
      return this.$store.getters['auth/getLoginInStatus']
    }
  }
}
</script>

<style scoped>
.centered-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.centered-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100px;
  width: 100%;
}

.form-floating {
  width: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type='email'] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type='password'] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.router-link-disabled {
  opacity: 0.5;
  pointer-events: none;
}
</style>
