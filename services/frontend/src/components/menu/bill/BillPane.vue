<template>
  <div class="card h-100 shadow-sm">
    <div class="card-header user-select-none">
      <div class="d-flex">
        <div class="text-danger"><i class="bi bi-printer cursor-pointer"> Print</i></div>
        <div class="mx-auto fw-bold fs-4">#{{ ordersToday + 1 }}</div>
        <div class="text-danger me-4 cursor-pointer"><i class="bi bi-copy me-2"></i>Copy</div>
        <div class="text-danger cursor-pointer" @click="clearBill">
          <i class="bi bi-trash me-2"></i>Clear
        </div>
      </div>
    </div>
    <div class="card-body">
      <div class="d-flex flex-column flex-shrink-0 container-fluid h-100">
        <div class="row pt-0">
          <div class="col">
            <!-- address and order type -->
            <div class="d-flex">
              <div class="col-auto d-block">
                <p class="m-0"><strong>Bill Gates</strong></p>
                <p class="mb-0 text-body-secondary">(555) 555-6666</p>
                <p class="mb-0 text-body-secondary">123 Main Street</p>
                <p class="mb-0 text-body-secondary">Belfast MA, 94122</p>
              </div>

              <div class="col-auto d-inline ms-auto">
                <span class="badge text-bg-secondary text-uppercase">{{
                  currentCart.items.orderType || 'DINE IN'
                }}</span>
              </div>
            </div>

            <!-- buttons 1 -->
            <div class="hstack gap-2 mt-3">
              <div class="dropdown-center col-6" id="orderNoteBtn">
                <button
                  class="btn btn-outline-secondary dropdown-toggle w-100"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Order Note
                </button>
                <div class="dropdown-menu shadow p-2">
                  <div class="input-group input-group-lg">
                    <textarea
                      v-model="orderNote"
                      class="form-control"
                      aria-label="With textarea"
                    ></textarea>
                    <button
                      class="btn btn-outline-secondary"
                      type="button"
                      id="button-addon1"
                      @click="addOrderNote"
                    >
                      Add Note
                    </button>
                  </div>
                </div>
              </div>
              <button type="button" class="btn btn-outline-secondary col-6">Discount</button>
            </div>
          </div>
          <span class="border-bottom border-secondary-subtle my-2"></span>
        </div>
        <div class="row mb-auto">
          <div
            class="col overflow-auto"
            style="max-height: calc(100vh / 2.4); overflow: auto; min-height: 100px"
          >
            <div v-if="currentCart.items[0]">
              <ul class="list-group list-group-flush">
                <BillItem
                  v-for="(item, index) in currentCart.items"
                  :id="index"
                  :key="item.id"
                  :item="item"
                />
              </ul>
            </div>
            <div v-else class="d-flex h-100 position-relative">
              <div class="position-absolute top-50 start-50 translate-middle">Add Items 🍕</div>
            </div>
          </div>
          <span class="border-bottom border-secondary-subtle my-2"></span>
        </div>

        <!-- row price -->
        <div class="row">
          <div class="col"><Bill_SubTotal /></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min.js'

import BillItem from './BillItem.vue'
import Bill_SubTotal from './BillPane_SubTotal.vue'

export default {
  components: { BillItem, Bill_SubTotal },
  data() {
    return {
      orderNote: ''
    }
  },

  methods: {
    clearBill() {
      this.$store.commit('orders/clearCurrentCart')
    },
    addOrderNote() {
      this.$store.commit('orders/setOrderNote', this.orderNote)

      // orderNoteBtn
      if (this.orderNote) {
        const orderNoteBtn = document.getElementById('orderNoteBtn')
        var tooltip = Tooltip.getInstance(orderNoteBtn)
        if (tooltip) {
          tooltip.setContent({ '.tooltip-inner': this.orderNote })
          tooltip.hide()
        } else {
          new Tooltip(orderNoteBtn, {
            placement: 'top',
            title: this.orderNote,
            html: true
          })
        }
      }
    }
  },
  computed: {
    currentCart() {
      return this.$store.getters['orders/getCurrentCart']
    },
    ordersToday() {
      return this.$store.getters['orders/getTotalOrdersToday']
    }
  }
}
</script>

<style scoped>
.dropdown-toggle::after {
  content: none;
}
</style>
