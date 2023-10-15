<template>
  <div class="container-fluid p-0">
    <div class="row row-cols-md-2">
      <div class="col p-2">
        <div class="card shadow d-flex">
          <div class="card-header">
            <div class="container">
              <div class="row">
                <div class="col-md-4 text-start p-1 text-body-secondary">
                  <i class="bi bi-search"> Search</i>
                </div>
                <div class="col-md-4 text-center fw-bold fs-4">Menu</div>
              </div>
            </div>
          </div>
          <div class="card-body p-1" style="overflow: hidden">
            <div class="container-fluid">
              <div class="row row-cols-md-2" style="height: calc(100vh - 80px)">
                <div class="col h-100 p-0 bg-body-secondary" style="overflow: auto">
                  <itemCard
                    title="1"
                    imageURL="https://www.funfoodfrolic.com/wp-content/uploads/2020/04/Bean-Salad-Thumbnail.jpg"
                  />
                  <itemCard title="2" />
                  <itemCard title="3" />
                  <itemCard title="4" />
                  <itemCard title="5" />
                  <itemCard title="6" />
                  <itemCard title="6" />
                  <itemCard title="6" />
                  <itemCard title="7" />
                </div>
                <div class="col h-100" style="overflow: auto">
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="ahahahh" />
                  <itemCard title="1" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col p-2 bg-secondary">
        <BillPane />
      </div>
    </div>
  </div>
</template>

<script>
import itemCard from '@/components/home/ItemCard.vue'
import BillPane from '@/components/home/BillPane.vue'
export default {
  components: { itemCard, BillPane }
}
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 100%;

  height: 58px;
  width: 60px;
}
</style>
