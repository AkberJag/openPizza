<template>
  <div class="h-100">
    <div class="card shadow d-flex">
      <div class="card-header">
        <div class="container">
          <div class="row">
            <div class="text-end p-1 d-flex justify-content-end">
              <div
                class="d-inline mx-3 text-body-secondary cursorPointer"
                @click="$emit('changeComponent', 'MenuPane')"
              >
                <i class="bi bi-x-square"></i> Cancel
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body p-1" style="overflow: hidden; height: calc(100vh - 73px)">
        <div class="container h-100">
          <div class="h-75">
            <div class="d-flex justify-content-center pt-5 align-items-center text-center">
              <div>
                <span class="fw-bold fs-5">Cash Payment Complete</span>
                <div class="card my-4 shadow-sm">
                  <div class="card-body">
                    <span class="fw-bold"> ${{ total }} - Paid </span>
                  </div>
                </div>
                <span class="fw-bold"> ${{ total }} Order Total</span>
              </div>
            </div>
          </div>
          <div class="h-25">
            <div class="d-grid gap-2 mx-2 pt-3">
              <button class="btn btn-danger" type="button">Print Receipt</button>
              <button class="btn btn-outline-danger" type="button">Close</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    cartItems() {
      const items = this.$store.getters['foodData/getCurrentCart']
      this.totalItems = items.items.length
      return items
    },
    total() {
      return this.cartItems.subTotal + this.cartItems.subTotal * this.cartItems.tax
    }
  }
}
</script>
