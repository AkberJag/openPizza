<template>
  <div class="col">
    <table class="table">
      <thead style="font-size: 0.8em">
        <tr>
          <th scope="col" style="max-width: 55px">Order Number</th>
          <th scope="col">Type</th>
          <th scope="col">Customer info</th>
          <th scope="col">Items</th>
          <th scope="col">Amount</th>
          <th scope="col">Eta</th>
          <th scope="col">Payments</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(order, index) in itemsOnHold" :key="index">
          <th>{{ order.id }}</th>
          <td>{{ order.orderType }}</td>
          <td>{{ order.customer }}</td>
          <td>{{ order.items.length }}</td>
          <td>${{ order.subTotal.toFixed(2) }}</td>
          <td>{{ Math.floor(Math.random() * 40) }} minutes</td>
          <td class="text-success">
            <i class="bi bi-cash-stack me-2"></i>
            <i class="bi bi-suit-heart-fill"></i>
          </td>
          <td>
            <div class="d-inline-flex gap-3">
              <button
                type="button"
                class="btn p-0"
                style="width: 2.5rem"
                @click="addBackToCartOrDelete({ id: order.id, action: 'move' })"
              >
                <i class="bi bi-cart-plus text-success"></i>
              </button>
              <button
                type="button"
                class="btn p-0"
                style="width: 2.5rem"
                @click="addBackToCartOrDelete({ id: order.id, action: 'delete' })"
              >
                <i class="bi bi-trash3 text-danger"></i>
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  methods: {
    addBackToCartOrDelete(payload) {
      this.$store.commit('orders/onHoldToCart', payload)
      if (payload.action === 'move') {
        this.$router.push({ name: 'MenuRoute' })
      }
    }
  },
  computed: {
    itemsOnHold() {
      return this.$store.getters['orders/getOrdersOnHold']
    }
  }
}
</script>
