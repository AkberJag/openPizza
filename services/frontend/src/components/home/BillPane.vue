<template>
  <div class="h-100">
    <div class="card shadow d-flex">
      <div class="card-header">
        <div class="container">
          <div class="row">
            <div class="col-md-4 text-start p-1 text-body-secondary">
              <i class="bi bi-printer cursorPointer"> Print</i>
            </div>
            <div class="col-md-4 text-center fw-bold fs-4">#9 ({{ totalItems }})</div>
            <div class="col-md-4 text-end p-1">
              <div class="d-inline mx-3 text-body-secondary cursorPointer">
                <i class="bi bi-copy"></i> Copy
              </div>
              <div class="d-inline text-body-secondary cursorPointer" @click="clearBill">
                <i class="bi bi-trash"></i> Clear
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body p-1" style="overflow: hidden; height: calc(100vh - 73px)">
        <div class="container">
          <div class="row row-cols-1 h-100">
            <!-- address -->
            <div class="col mt-2">
              <div class="card shadow-sm" style="overflow: auto; height: calc((100vh - 180px) / 3)">
                <div class="card-body p-2 ms-2" style="overflow: auto">
                  <span class="badge text-bg-secondary float-end me-2 text-uppercase">{{
                    cartItems.orderType
                  }}</span>
                  <p class="m-0"><strong>Bill Gates</strong></p>
                  <p class="mb-0 text-body-secondary">(555) 555-6666</p>
                  <p class="mb-0 text-body-secondary">123 Main Street</p>
                  <p class="mb-0 text-body-secondary">Belfast MA, 94122</p>
                </div>
                <div class="card-footer bg-transparent pt-1 pb-1">
                  <div class="d-grid gap-2 d-md-flex">
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-stickies mx-2"></i> Order Note
                    </button>
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-patch-check mx-2"></i>Discount
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- items -->
            <div class="col mt-2">
              <div class="card shadow-sm">
                <div class="card-body" style="overflow: auto; height: calc((100vh - 120px) / 3)">
                  <table class="table table-hover">
                    <tbody>
                      <BillItem
                        v-for="(item, index) in cartItems.items"
                        :key="index"
                        :count="index"
                        :item="item"
                      />
                    </tbody>
                  </table>
                </div>
                <div class="card-footer bg-transparent pt-1 pb-1">
                  <div class="d-grid gap-2 d-md-flex">
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-pencil mx-2"></i>Modify
                    </button>
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-sticky mx-2"></i> Add Note
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- amount -->
            <div class="col mt-2 mb-5" style="overflow: auto; height: calc((100vh - 220px) / 3)">
              <div class="list-group h-100 shadow-sm">
                <div
                  class="shadow-sm list-group-item list-group-item-action d-flex justify-content-between"
                >
                  <div class="text-success ms-2">+ Add delivery charge</div>
                  <div class="text-success me-2">+ Add extra charge</div>
                </div>
                <div
                  class="list-group-item list-group-item-action d-flex justify-content-between list-group-item-secondary p-1 px-3"
                >
                  <div class="text-dark-emphasis ms-2">Subtotal</div>
                  <div class="text-dark-emphasis me-2 pe-2 fw-bold">
                    ${{ subTotal_tweened.toFixed(2) }}
                  </div>
                </div>
                <div
                  class="list-group-item list-group-item-action d-flex justify-content-between list-group-item-secondary p-1 px-3"
                >
                  <div class="text-dark-emphasis ms-2 me-3" for="flexSwitchCheckChecked">Tax</div>
                  <div class="form-check form-switch me-auto mt-1">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      role="switch"
                      id="flexSwitchCheckChecked"
                      v-model="toggleTax"
                    />
                  </div>
                  <div class="text-dark-emphasis me-2 pe-2" :class="{ 'fw-bold': toggleTax }">
                    ${{ taxAmount_tweened.toFixed(2) }}
                  </div>
                </div>
                <div class="list-group-item d-flex justify-content-between d-grid gap-2 shadow-sm">
                  <button type="button" class="btn btn-secondary col-4">Hold</button>
                  <button type="button" class="btn btn-danger col-8">Pay</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gsap from 'gsap'

import BillItem from './BillItem.vue'
export default {
  components: { BillItem },

  data() {
    return {
      toggleTax: false,
      taxPercentage: 0.2,
      totalItems: 0,

      subTotal_tweened: 0,
      taxAmount_tweened: 0
    }
  },

  methods: {
    clearBill() {
      this.$store.commit('foodData/clearCurrentCart')
    }
  },

  computed: {
    cartItems() {
      const items = this.$store.getters['foodData/getCurrentCart']
      this.totalItems = items.items.length
      return items
    },
    subTotal() {
      return this.toggleTax
        ? this.cartItems.subTotal + this.cartItems.subTotal * this.taxPercentage
        : this.cartItems.subTotal
    },
    taxAmount() {
      return this.cartItems.subTotal * this.taxPercentage
    }
  },

  watch: {
    subTotal(n) {
      gsap.to(this, { duration: 0.5, subTotal_tweened: Number(n) || 0 })
    },
    taxAmount(n) {
      gsap.to(this, { duration: 0.5, taxAmount_tweened: Number(n) || 0 })
    }
  }
}
</script>

<style scoped>
li {
  padding-left: 2em;
  margin-bottom: 1em;
}
.cursorPointer {
  cursor: pointer;
}
</style>
