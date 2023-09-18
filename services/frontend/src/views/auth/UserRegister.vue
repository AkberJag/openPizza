<template>
  <div class="bg-body-tertiary w-100 body">
    <main class="form-signin w-100 m-auto">
      <div class="centered-container">
        <form class="centered-form">
          <p style="font-size: 8cap">🍕</p>
          <h1 class="h3 mb-3 fw-normal">Please Register</h1>

          <div class="form-floating">
            <input type="text" class="form-control" id="floatingInputName" placeholder="my name" />
            <label for="floatingInputName">Full Name</label>
          </div>
          <div class="form-floating">
            <input
              type="email"
              class="form-control"
              id="floatingInput"
              placeholder="name@example.com"
            />
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating">
            <input
              type="password"
              class="form-control"
              id="floatingPassword"
              placeholder="Password"
            />
            <label for="floatingPassword">Password</label>
          </div>
          <button class="btn btn-primary w-100 py-2 mt-4" type="submit">Register</button>
        </form>
      </div>
    </main>
  </div>
</template>

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
