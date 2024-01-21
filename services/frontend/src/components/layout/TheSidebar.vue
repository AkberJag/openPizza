<template>
  <div class="d-flex flex-column flex-shrink-0 text-bg-dark vh-100" style="width: 4.5rem">
    <div class="text-center user-select-none" style="font-size: xxx-large">🍕</div>

    <ul class="nav nav-pills mb-auto text-center overflow-auto mt-3">
      <!-- Menus -->
      <li class="nav-item cursor-pointer">
        <router-link
          :to="{ name: 'MenuRoute' }"
          class="nav-link py-3 border-bottom border-secondary rounded-0"
          data-bs-toggle="tooltip"
          data-bs-title="Menus 🍕"
        >
          <i class="bi bi-pencil-square"></i>
        </router-link>
      </li>

      <!-- orders -->
      <li class="nav-item cursor-pointer">
        <router-link
          :to="{ name: 'OrdersRoute' }"
          class="nav-link py-3 border-bottom border-secondary rounded-0"
          data-bs-toggle="tooltip"
          data-bs-title="Orders 📃"
        >
          <i class="bi bi-journals"></i>
        </router-link>
      </li>

      <!-- Customers -->
      <li class="nav-item cursor-pointer">
        <a
          class="nav-link py-3 border-bottom border-secondary rounded-0"
          data-bs-toggle="tooltip"
          data-bs-title="Customers 🧑‍🤝‍🧑"
        >
          <i class="bi bi-people"></i>
        </a>
      </li>

      <li class="nav-item cursor-pointer">
        <a
          class="nav-link py-3 border-bottom border-secondary rounded-0"
          data-bs-toggle="tooltip"
          data-bs-title="Cash Management 💰"
        >
          <i class="bi bi-cash-stack"></i>
        </a>
      </li>

      <li class="nav-item cursor-pointer">
        <a
          class="nav-link py-3 border-bottom border-secondary rounded-0"
          data-bs-toggle="tooltip"
          data-bs-title="Delivery Management 🚚"
        >
          <i class="bi bi-truck"></i>
        </a>
      </li>
    </ul>

    <!-- settings -->
    <div
      class="dropdown border-top border-secondary p-3 text-center cursor-pointer dropdown-toggle"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <i class="bi bi-person-circle" data-bs-toggle="tooltip" data-bs-title="User settings 🔧"></i>
    </div>
    <ul class="dropdown-menu p-2 ms-5 rounded-3 shadow" data-bs-theme="dark">
      <li>
        <h6 class="dropdown-header">
          <i class="bi bi-person-circle me-2 text-muted"></i>
          {{ userName }}
        </h6>
      </li>

      <li>
        <router-link
          :to="{ name: 'AddItemsRoute' }"
          class="dropdown-item rounded-2 d-flex gap-2 align-items-center cursor-pointer"
        >
          <i class="bi bi-diagram-3-fill"></i>Add new
        </router-link>
      </li>
      <li>
        <a
          class="dropdown-item rounded-2 d-flex gap-2 align-items-center cursor-pointer"
          @click="changeTheme"
        >
          <i class="bi bi-brightness-low-fill"></i>Toggle theme</a
        >
      </li>
      <li><hr class="dropdown-divider" /></li>
      <li>
        <a class="dropdown-item rounded-2 d-flex gap-2 align-items-center" @click="logout"
          ><i class="bi bi-box-arrow-left"></i>Logout</a
        >
      </li>
    </ul>
  </div>
</template>

<script>
import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min.js'

export default {
  mounted() {
    new Tooltip(document.body, {
      selector: "[data-bs-toggle='tooltip']",
      trigger: 'hover'
    })
  },
  methods: {
    changeTheme() {
      this.$store.commit('setTheme')
      this.$emit('themeChange', this.$store.getters.getTheme)
    },
    async logout() {
      await this.$store.dispatch('auth/logout')
    }
  },
  computed: {
    userName() {
      return this.$store.getters['auth/getuserName']
    }
  }
}
</script>

<style scoped>
.nav-item,
.dropdown {
  background-color: initial;
  transition: background-color 0.5s ease;
  width: 100%;
}

.nav-item:hover,
.dropdown:hover {
  background-color: var(--bs-primary-text-emphasis);
}

.bi {
  color: var(--bs-light);
  font-size: larger;
}

:after {
  content: none;
}

.dropdown-item:hover {
  background-color: var(--bs-primary);
}
</style>
