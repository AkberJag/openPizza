<template>
  <div
    class="d-flex flex-column flex-shrink-0 bg-body-tertiary min-vh-100"
    style="width: 4.5rem"
    v-if="isLoggedIn"
  >
    <div class="text-center" style="font-size: xxx-large">🍕</div>
    <ul class="nav nav-pills flex-column mb-auto text-center">
      <!-- menus -->
      <li>
        <router-link
          :to="{ name: 'HomeRoute' }"
          class="nav-link py-3 border-bottom border-top"
          aria-current="page"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Home"
        >
          <i class="bi bi-pencil-square"></i>
        </router-link>
      </li>
      <!-- orders -->
      <li>
        <router-link
          :to="{ name: 'OrdersRoute' }"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Dashboard"
        >
          <i class="bi bi-journals"></i>
        </router-link>
      </li>
      <!-- Customers -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Orders"
        >
          <i class="bi bi-people"></i>
        </a>
      </li>
      <!-- Cash Management -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Products"
        >
          <i class="bi bi-cash-stack"></i>
        </a>
      </li>
      <!-- Delivery Management (Optional Feature) -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Customers"
        >
          <i class="bi bi-truck"></i>
        </a>
      </li>
    </ul>

    <!-- Settings -->
    <div class="dropdown border-top">
      <a
        href="#"
        class="d-flex align-items-center justify-content-center p-3 text-decoration-none dropdown-toggle"
        id="dropdownUser3"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <i class="bi bi-person-circle"></i>
      </a>
      <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser3">
        <li><a class="dropdown-item" href="#">New project...</a></li>
        <li><a class="dropdown-item" href="#">Settings</a></li>
        <li>
          <a class="dropdown-item" @click="changeTheme" style="cursor: pointer"
            >Disable {{ currentTheme }} mode</a
          >
        </li>
        <li><hr class="dropdown-divider" /></li>
        <li><a class="dropdown-item" href="#" @click="logout">Sign out</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentTheme: this.$store.getters.getTheme
    }
  },
  methods: {
    changeTheme() {
      this.$store.commit('setTheme')
      this.currentTheme = this.$store.getters.getTheme
      this.$emit('themeChange', this.currentTheme)
    },
    async logout() {
      await this.$store.dispatch('auth/logout')
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters['auth/isAuthenticated']
    }
  }
}
</script>

<style scoped>
.nav-link {
  border-radius: 0;
}

.bi {
  font-size: 1.5rem;
}
</style>
