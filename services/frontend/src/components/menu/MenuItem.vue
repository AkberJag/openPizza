<template>
  <div
    class="card mb-2 mb-md-3 cursor-pointer user-select-none"
    :class="selected ? 'shadow border-secondary border-2' : 'shadow-sm'"
  >
    <div class="card-body text-center" :class="{ 'd-flex': price }">
      <div class="text-center flex-fill">{{ title }}</div>
      <div v-if="price" class="ms-auto text-muted">${{ price }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'selected', 'price']
}
</script>
