<template>
  <div class="bg-body-tertiary w-100 body">
    <main class="form-signin w-100 m-auto">
      <div class="centered-container">
        <form class="centered-form" @submit.prevent="submitForm">
          <p style="font-size: 8cap">🍕</p>
          <h1 class="h3 mb-3 fw-normal">Please Register</h1>

          <div class="form-floating">
            <input
              type="text"
              class="form-control"
              id="floatingInputName"
              placeholder="my name"
              required
              v-model="fullname"
            />
            <label for="floatingInputName">Full Name</label>
          </div>
          <div class="form-floating">
            <input
              type="email"
              class="form-control"
              id="floatingInput"
              placeholder="name@example.com"
              v-model="email"
            />
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="Password"
              v-model="password"
            />
            <label for="floatingPassword">Password</label>
          </div>
          <button class="btn btn-primary w-100 py-2 mt-4" type="submit">Register</button>
          <router-link
            :to="{ name: 'LoginRoute' }"
            class="link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover mt-3"
          >
            or Login
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
      fullname: '',
      email: '',
      password: ''
    }
  },
  methods: {
    async submitForm() {
      await this.$store.dispatch('register', {
        fullname: this.fullname,
        email: this.email,
        password: this.password
      })
    }
  }
}
</script>

<style scoped>
.body {
  position: fixed;
  left: 0;
  height: 100%;
}

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
  border-radius: 0;
}
.form-signin input[type='text'] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type='password'] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
