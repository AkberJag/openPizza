<template>
  <div class="container-fluid">
    <div class="row flex-wrap-reverse mt-3">
      <div class="col col-12 col-md-10">
        <ul
          class="nav nav-pills nav-fill gap-2 p-1 small bg-body-secondary rounded-2 shadow-sm border"
          id="pillNav2"
          style="
            --bs-nav-link-color: var(--bs-tertiary-color);
            --bs-nav-link-hover-color: var(--bs-emphasis-color);
            --bs-nav-pills-link-active-color: var(--bs-tertiary);
            --bs-nav-pills-link-active-bg: var(--bs-white);
          "
        >
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active rounded-2"
              id="home-tab2"
              data-bs-toggle="tab"
              type="button"
              role="tab"
              @click="component = 'OnHoldComponent'"
            >
              On Hold ({{ itemsOnHold.length }})
            </button>
          </li>

          <li class="nav-item" role="presentation">
            <button
              class="nav-link rounded-2"
              id="contact-tab2"
              data-bs-toggle="tab"
              type="button"
              role="tab"
              @click="component = 'CompletedOrdersComponent'"
            >
              Complete ({{ totalOrders }})
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <router-link
              class="nav-link rounded-2"
              type="button"
              role="tab"
              :to="{ name: 'MenuRoute' }"
              >New</router-link
            >
          </li>
        </ul>
      </div>
      <div class="col"></div>
    </div>
    <div class="row mt-2">
      <transition name="component" mode="out-in">
        <component :is="component"></component>
      </transition>
    </div>
  </div>
</template>

<script>
import OnHoldComponent from '@/components/orders/OnHold.vue'
import CompletedOrdersComponent from '@/components/orders/CompletedOrders.vue'
export default {
  components: { OnHoldComponent, CompletedOrdersComponent },

  data() {
    return {
      component: 'OnHoldComponent'
    }
  },

  computed: {
    itemsOnHold() {
      return this.$store.getters['orders/getOrdersOnHold']
    },
    totalOrders() {
      return this.$store.getters['orders/getTotalOrders']
    }
  }
}
</script>
