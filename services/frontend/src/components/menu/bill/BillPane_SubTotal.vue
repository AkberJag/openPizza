<template>
  <div>
    <ul class="list-group shadow">
      <li class="list-group-item d-flex">
        <TotalTopButtons
          class="me-auto"
          isReasonRequired="false"
          :title="deliveryTitle"
          :prices="TotalTopButtonPrices1"
          @addAmount="addDeliveryCharge"
        />

        <TotalTopButtons
          id="extraChargeBtn"
          isReasonRequired="true"
          :title="extraChargeTitle"
          :prices="TotalTopButtonPrices2"
          @addAmount="addExtraCharge"
        />
      </li>
      <li class="list-group-item d-flex bg-body-tertiary">
        <div class="fw-semibold me-auto">Sub Total</div>
        <div class="fw-semibold">${{ subTotal_tweened.toFixed(2) }}</div>
      </li>
      <li class="list-group-item d-flex bg-body-tertiary">
        <div class="fw-semibold me-auto">
          <div class="d-flex">
            <label class="form-check-label me-3" for="taxCheck">Tax</label>
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                id="taxCheck"
                :disabled="disabledAmntBtns"
                v-model="toggleTax"
              />
            </div>
          </div>
        </div>
        <div :class="toggleTax ? 'fw-semibold' : 'text-muted'">${{ taxAmount }}</div>
      </li>
    </ul>
    <div class="hstack gap-2 mt-3">
      <button
        type="button"
        class="btn btn-secondary col-3 position-relative"
        :disabled="disabledAmntBtns || leftPaneComponent === 'OrderCompletePane'"
        @click="holdCurrentOrder"
      >
        Hold
        <span
          v-if="itemsOnHold"
          class="position-absolute top-0 start-0 translate-middle badge rounded-pill bg-primary"
          >{{ itemsOnHold }}</span
        >
      </button>
      <button
        type="button"
        class="btn btn-danger col"
        :disabled="disabledAmntBtns || leftPaneComponent === 'OrderCompletePane'"
        @click="changeLeftComponent('OrderCompletePane')"
      >
        Pay
      </button>
    </div>
  </div>
</template>

<script>
import gsap from 'gsap'
import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min.js'

import TotalTopButtons from './TotalTopButtons.vue'
export default {
  components: { TotalTopButtons },
  data() {
    return {
      TotalTopButtonPrices1: [2, 5, 10, 15],
      TotalTopButtonPrices2: [5, 10, 15],

      subTotal_tweened: 0,
      toggleTax: false,
      taxPercentage: 0.25
    }
  },
  methods: {
    addDeliveryCharge(payload) {
      this.$store.commit('orders/addDeliveryCharge', payload.price)
    },

    addExtraCharge(payload) {
      this.$store.commit('orders/addExtraCharge', payload)

      // for tooltip
      if (payload.price != 0) {
        const extraChargeBtn = document.getElementById('extraChargeBtn')
        var tooltip = Tooltip.getInstance(extraChargeBtn)
        if (tooltip) {
          tooltip.setContent({ '.tooltip-inner': this.extraChargeReason })
          tooltip.hide()
        } else {
          new Tooltip(extraChargeBtn, {
            placement: 'bottom',
            title: this.extraChargeReason,
            html: true
          })
        }
      } else {
        const extraChargeBtn = document.getElementById('extraChargeBtn')
        var tooltipInstance = Tooltip.getInstance(extraChargeBtn)
        if (tooltipInstance) {
          tooltipInstance.dispose()
        }
      }
    },

    holdCurrentOrder() {
      this.$store.commit('orders/holdCurrentOrder')
      this.$store.commit('orders/clearCurrentCart')
    },

    changeLeftComponent(pane) {
      this.$store.commit('foodMenu/setLeftPaneComponent', pane)
    },

    changeRightComponent(pane) {
      this.$store.commit('foodMenu/setRightPaneComponent', pane)
    }
  },
  computed: {
    currentCart() {
      return this.$store.getters['orders/getCurrentCart']
    },

    subTotal() {
      return this.toggleTax
        ? this.currentCart.subTotal + this.currentCart.subTotal * this.currentCart.tax
        : this.currentCart.subTotal
    },

    deliveryTitle() {
      let charge = this.$store.getters['orders/getDeliveryCharge']
      if (charge != 0) {
        return 'Delivery charge: $' + charge
      }
      return '+ Add delivery charge'
    },

    extraChargeTitle() {
      let charge = this.$store.getters['orders/getExtraCharge']
      if (charge.price != 0) {
        return 'Extra charge: $' + charge.price
      }
      return '+ Add extra charge'
    },

    extraChargeReason() {
      let charge = this.$store.getters['orders/getExtraCharge']
      if (charge.reason != '') {
        return charge.reason
      }
      return 'Add extra charge'
    },

    disabledAmntBtns() {
      return this.currentCart.items.length === 0
    },
    taxAmount() {
      return this.currentCart.subTotal * this.taxPercentage
    },
    itemsOnHold() {
      return this.$store.getters['orders/getOrdersOnHold'].length
    },

    leftPaneComponent() {
      return this.$store.getters['foodMenu/getLeftPaneComponent']
    }
  },
  watch: {
    subTotal(n) {
      gsap.to(this, { duration: 0.5, subTotal_tweened: Number(n) || 0 })
    },
    toggleTax(val) {
      if (val) {
        this.$store.commit('orders/setTax', this.taxPercentage)
      } else {
        this.$store.commit('orders/setTax', 0)
      }
    }
  }
}
</script>
