<template>
  <div class="card m-3 shadow-sm" style="max-height: 60px">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="imageURL" class="img-fluid rounded-start" alt="" />
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <p class="card-text">{{ title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['imageURL', 'title']
}
</script>

<style scoped>
img {
  height: 58px;
}
.card {
  cursor: pointer;
}
</style>
