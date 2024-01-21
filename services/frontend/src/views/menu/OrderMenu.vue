<template>
  <div class="d-flex flex-wrap h-100 p-2">
    <div class="pe-md-1 col-12 col-md-6 mb-2 mb-md-0">
      <transition name="component" mode="out-in">
        <component :is="leftPaneComponent"></component>
      </transition>
    </div>
    <div class="ps-md-1 col-12 col-md-6">
      <transition name="component" mode="out-in">
        <KeepAlive>
          <component :is="rightPaneComponent"></component>
        </KeepAlive>
      </transition>
    </div>
  </div>
</template>

<script>
import MenuPane from '@/components/menu/MenuPane.vue'
import BillPane from '@/components/menu/bill/BillPane.vue'
import OrderCompletePane from '@/components/menu/orderComplete/OrderComplete.vue'

export default {
  components: { MenuPane, BillPane, OrderCompletePane },

  computed: {
    leftPaneComponent() {
      return this.$store.getters['foodMenu/getLeftPaneComponent']
    },
    rightPaneComponent() {
      return this.$store.getters['foodMenu/getRightPaneComponent']
    }
  }
}
</script>

<style scoped></style>
