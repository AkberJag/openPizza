<template>
  <div class="d-flex vh-100">
    <transition name="slide">
      <div v-if="isLoggedIn" class="flex-shrink-1">
        <TheSidebar @themeChange="themeChange" />
      </div>
    </transition>
    <TheToastContainer />
    <div class="w-100">
      <router-view v-slot="{ Component }">
        <transition name="route" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </div>
</template>
<script>
import { Popover } from 'bootstrap/dist/js/bootstrap.esm.min.js'
import TheSidebar from './components/layout/TheSidebar.vue'
import TheToastContainer from './components/layout/TheToastContainer.vue'

export default {
  components: { TheSidebar, TheToastContainer },
  mounted() {
    // Set app theme
    document.body.setAttribute('data-bs-theme', this.$store.getters.getTheme)
  },
  methods: {
    themeChange(val) {
      document.body.setAttribute('data-bs-theme', val)
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters['auth/isAuthenticated']
    }
  }
}
</script>

<style>
.cursor-pointer {
  cursor: pointer;
}

/* main animation */
.route-leave-from,
.route-enter-to {
  opacity: 1;
}

.route-enter-from,
.route-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

.route-enter-active {
  transition: all 0.3s ease-in;
}

.route-leave-active {
  transition: all 0.3s ease-out;
}

/* sidebar animation */
/* anmation */
.slide-leave-from,
.slide-enter-to {
  width: 4.5rem;
}

.slide-enter-from,
.slide-leave-to {
  width: 0rem;
}

.slide-enter-active {
  transition: all 0.3s ease;
}

.slide-leave-active {
  transition: all 0.3s ease;
}

/* components animation */
.component-leave-from,
.component-enter-to {
  opacity: 1;
}
.component-enter-from,
.component-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.component-enter-active {
  transition: all 0.3s ease-in;
}
.component-leave-active {
  transition: all 0.3s ease-out;
}
</style>
