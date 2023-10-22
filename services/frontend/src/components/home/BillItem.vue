<template>
  <tr>
    <th scope="row" class="fs-6">{{ count + 1 }}</th>
    <td class="col-11">
      <div class="row me-0">
        <div class="fw-bold text-capitalize fs-6 col-10 m-0" style="cursor: pointer" @click="test">
          {{ item.item_name }}
          <span class="right-icon ms-auto" :class="{ 'right-icon-rotate': rotateArrow }">
            <i class="bi bi-chevron-down"></i>
          </span>
        </div>
        <div class="fw-bold text-end col-2">${{ item.price }}</div>
      </div>
      <div class="collapse m-0" :id="count">
        <div class="row me-0">
          <div class="col-10">
            <span class="me-2 text-danger" style="opacity: 75%">Type</span>
            <span class="text-body-secondary">Dinner</span>
          </div>
          <div class="col-2 text-end text-body-secondary">${{ item.price }}</div>
        </div>
      </div>
    </td>
  </tr>
</template>

<script>
import { Collapse } from 'bootstrap/dist/js/bootstrap.esm.min.js'
export default {
  props: ['count', 'item'],

  mounted() {
    const collapseElement = document.getElementById(this.count)
    this.collapseInstance = new Collapse(collapseElement, { toggle: false })
  },

  data() {
    return {
      collapseInstance: null,
      rotateArrow: false
    }
  },

  methods: {
    test() {
      this.collapseInstance.toggle()
      this.rotateArrow = !this.rotateArrow
    }
  }
}
</script>

<style scoped>
.right-icon {
  display: inline-flex;
  transition: all 0.3s;
  opacity: 50%;
}

.right-icon-rotate {
  transform: rotate(180deg);
}
</style>
