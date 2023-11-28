<template>
  <div class="container-fluid p-0">
    <div class="row">
      <div class="col col-5 p-2">
        <transition name="component" mode="out-in">
          <component @changeComponent="changeComponent" :is="leftPaneComponent"></component>
        </transition>
      </div>
      <div class="col p-2">
        <transition name="component" mode="out-in">
          <KeepAlive>
            <component @changeComponent="changeComponent" :is="rightPaneComponent"></component>
          </KeepAlive>
        </transition>
      </div>
    </div>
  </div>
</template>
<script>
import OrderDetails from '@/components/orders/OrderDetails.vue'
import OrderList from '@/components/orders/OrderList.vue'

import { computed } from 'vue'

export default {
  components: { OrderDetails, OrderList },
  provide() {
    return {
      leftPaneComponent: computed(() => this.leftPaneComponent)
    }
  },
  data() {
    return {
      leftPaneComponent: 'OrderList',
      rightPaneComponent: 'OrderDetails'
    }
  },
  methods: {
    changeComponent(payload) {
      this.leftPaneComponent = payload
    }
  }
}
</script>
