<template>
  <div class="container-fluid p-0">
    <div class="row row-cols-md-2">
      <div class="col p-2">
        <transition name="component" mode="out-in">
          <component :is="leftPaneComponent"></component>
        </transition>
      </div>
      <div class="col p-2 bg-secondary">
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
import BillPane from '@/components/home/BillPane.vue'
import MenuPane from '@/components/home/MenuPane.vue'
import OrderComplete from '@/components/home/OrderComplete.vue'

export default {
  components: { BillPane, MenuPane, OrderComplete },
  data() {
    return {
      leftPaneComponent: 'MenuPane',
      rightPaneComponent: 'BillPane'
    }
  },
  methods: {
    changeComponent(payload) {
      this.rightPaneComponent = payload
    }
  }
}
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 100%;

  height: 58px;
  width: 60px;
}

.component-leave-from,
.component-enter-to {
  opacity: 1;
}
.component-enter-from,
.component-leave-to {
  opacity: 0;
  transform: scale(0.9);
}
.component-enter-active {
  transition: all 0.3s ease-in;
}
.component-leave-active {
  transition: all 0.3s ease-out;
}
</style>
