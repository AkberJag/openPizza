<template>
  <div class="d-flex">
    <div class="dropup">
      <div
        :id="'priceDropdown' + isReasonRequired"
        class="dropdown-toggle text-success cursor-pointer"
        data-bs-toggle="dropdown"
        data-bs-auto-close="outside"
      >
        {{ title }}
      </div>
      <div class="dropdown-menu shadow-lg border-secondary border-opacity-75">
        <h6 class="dropdown-header text-center">{{ title }}</h6>

        <div class="d-flex flex-column">
          <!-- reason input box -->
          <div class="mx-2">
            <input
              v-if="isReasonRequired === 'true'"
              type="text"
              placeholder="reason (required)"
              class="form-control"
              v-model="reason"
              v-on:keyup.enter="this.$refs.price.focus()"
            />
          </div>
          <!-- predefined prices -->
          <div class="btn-group m-2">
            <button
              type="button"
              class="btn btn-outline-primary"
              v-for="(price, index) in prices"
              :key="index"
              @click="onClickButton(price)"
              :disabled="
                (isReasonRequired === 'true' && reason === '') ||
                (isReasonRequired === 'false' && reason !== '')
              "
            >
              ${{ price }}
            </button>
          </div>

          <!-- customer price input -->
          <div class="input-group px-2" style="min-width: max-content">
            <input
              min="0"
              ref="price"
              type="number"
              class="form-control"
              placeholder="$ Enter amount (required)"
              v-model.number="customPrice"
              v-on:keyup.enter="this.$refs.addBtn.focus()"
            />

            <!-- add button -->
            <button
              class="btn btn-outline-success"
              type="button"
              ref="addBtn"
              @click="onClickButton(customPrice)"
              :disabled="
                !(
                  (customPrice > 0 && isReasonRequired === 'true' && reason !== '') ||
                  (customPrice > 0 && !(isReasonRequired === 'true') && !(reason !== '')) ||
                  (!(customPrice > 0) && isReasonRequired === 'true' && !(reason !== ''))
                )
              "
            >
              Add
            </button>
          </div>
        </div>
      </div>
    </div>
    <button type="button" class="btn p-0" style="width: 2.5rem" @click="onClickButton(0)">
      <i class="bi bi-x-circle text-danger" style="--bs-text-opacity: 0.5"></i>
    </button>
  </div>
</template>

<script>
import { Dropdown } from 'bootstrap/dist/js/bootstrap.esm.min.js'

export default {
  props: ['title', 'prices', 'isReasonRequired'],
  data() {
    return {
      reason: '',
      customPrice: 0.1
    }
  },
  methods: {
    onClickButton(price) {
      if ((typeof this.customPrice == 'number') & (this.customPrice > 0)) {
        this.$emit('addAmount', { price: price, reason: this.reason })
        this.customPrice = 0.1
        this.reason = ''
      } else {
        this.customPrice = 0.1
      }

      // close dropdown
      const priceDropdown = document.getElementById('priceDropdown' + this.isReasonRequired)
      var dropdownInstance = Dropdown.getInstance(priceDropdown)
      if (dropdownInstance) {
        dropdownInstance.hide()
        dropdownInstance.update()
      }
    }
  }
}
</script>

<style scoped>
.dropdown-toggle::after {
  content: none;
}
</style>
