<template>
  <div class="card h-100 shadow-sm">
    <div class="card-header user-select-none">
      <div class="d-flex cursor-pointer" @click="changeLeftComponent('MenuPane')">
        <i class="bi bi-x-square me-3 ms-auto"></i> Cancel
      </div>
    </div>
    <div class="card-body">
      <div class="d-flex flex-column h-100 text-center">
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
              class="nav-link rounded-2"
              id="home-tab2"
              data-bs-toggle="tab"
              type="button"
              role="tab"
              @click="paymentMethod = 'Card'"
            >
              Card
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active rounded-2"
              id="profile-tab2"
              data-bs-toggle="tab"
              type="button"
              role="tab"
              @click="paymentMethod = 'Cash'"
            >
              Cash
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link rounded-2"
              id="contact-tab2"
              data-bs-toggle="tab"
              type="button"
              role="tab"
              @click="paymentMethod = 'Other'"
            >
              Other
            </button>
          </li>
        </ul>
        <div class="mt-5 fs-5 fw-bold">Make {{ paymentMethod }} payment</div>
        <div class="mt-2 fs-1 fw-bold">${{ total.toFixed(2) }}</div>
        <div class="mt-auto d-grid gap-2">
          <button class="btn btn-danger">Print Receipt</button>
          <button type="button" class="btn btn-outline-danger" @click="placeOrder">Complete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      paymentMethod: 'Cash'
    }
  },
  methods: {
    async placeOrder() {
      await this.$store.dispatch('orders/placeOrder')
      this.$store.commit('orders/clearCurrentCart')
      this.changeLeftComponent('MenuPane')
    },
    changeLeftComponent(pane) {
      this.$store.commit('foodMenu/setLeftPaneComponent', pane)
    }
  },
  computed: {
    total() {
      let current_cart = this.$store.getters['orders/getCurrentCart']
      return current_cart.subTotal + current_cart.subTotal * current_cart.tax
    }
  }
}
</script>
