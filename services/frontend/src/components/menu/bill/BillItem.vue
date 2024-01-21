<template>
  <li class="list-group-item">
    <div class="d-flex fw-bold mb-2">
      <div
        class="hstack flex-fill me-auto collapsed cursor-pointer"
        data-bs-toggle="collapse"
        :data-bs-target="'#i' + id"
      >
        <div class="me-4">{{ id + 1 }}.</div>
        <div class="me-2">{{ item.name }}</div>
        <i class="bi bi-chevron-up rotate"></i>
      </div>

      <div v-if="leftPaneComponent !== 'OrderCompletePane'" class="hstack text-muted gap-3 me-4">
        <!-- trash btn -->
        <button type="button" class="btn p-0" style="width: 2.5rem" @click="onClickButton(0)">
          <i class="bi bi-trash3 text-danger" style="--bs-text-opacity: 0.5"></i>
        </button>

        <!--  + btn -->
        <button type="button" class="btn p-0" style="width: 2.5rem" @click="onClickButton(1)">
          <i class="bi bi-plus-circle text-muted" style="--bs-text-opacity: 0.5"></i>
        </button>

        <!-- qty text -->
        <div class="text-center" style="min-width: 40px">x{{ item.qty }}</div>

        <!-- - btn -->
        <button type="button" class="btn p-0" style="width: 2.5rem" @click="onClickButton(-1)">
          <i class="bi bi-dash-circle text-muted" style="--bs-text-opacity: 0.5"></i>
        </button>
      </div>
      <div class="text-end" style="min-width: 70px">
        ${{ totalPrice_tweened ? totalPrice_tweened.toFixed(2) : totalPrice.toFixed(2) }}
      </div>
    </div>

    <!-- collapse -->
    <div
      class="collapse ms-4 ps-3"
      :id="'i' + id"
      data-bs-toggle="collapse"
      :data-bs-target="'#i' + id"
    >
      <div class="d-flex">
        <span class="text-danger">
          Type:
          <span class="text-muted">{{ item.categoryName }}</span>
        </span>
        <div class="ms-auto text-muted">${{ item.price }}</div>
      </div>
    </div>
  </li>
</template>

<script>
import gsap from 'gsap'

export default {
  props: ['item', 'id'],
  data() {
    return {
      totalPrice_tweened: 0
    }
  },
  methods: {
    onClickButton(val) {
      this.$store.commit('orders/removeItemFromCurrentCart', { itemId: this.item.id, val })
    }
  },
  computed: {
    totalPrice() {
      return this.item.qty * this.item.price
    },
    leftPaneComponent() {
      return this.$store.getters['foodMenu/getLeftPaneComponent']
    }
  },
  watch: {
    totalPrice(n) {
      gsap.to(this, { duration: 0.5, totalPrice_tweened: Number(n) || 0 })
    }
  }
}
</script>

<style scoped>
/* Rotate icon when the collapse is shown */
.rotate {
  transition: transform 0.4s;
}

.collapsed .rotate {
  transform: rotate(180deg);
}
</style>
