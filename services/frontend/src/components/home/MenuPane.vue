<template>
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
            <div v-if="filteredFoodData.length > 0">
              <itemCard
                v-for="category in filteredFoodData"
                :key="category.categoryID"
                :title="category.categoryName"
                :imageURL="category.categoryImageURL"
                :selected="category.categoryID === selectedCategory"
                @click="loadItems(category.categoryID), (selectedCategory = category.categoryID)"
              />
            </div>
            <div v-else class="m-2 d-flex justify-content-center">
              <base-spinner></base-spinner>
            </div>
          </div>
          <div class="col h-100" style="overflow: auto">
            <div
              class="m-2 d-flex justify-content-center"
              v-if="items.length === 0 && loadingItems"
            >
              <base-spinner></base-spinner>
            </div>
            <div class="m-2 d-flex justify-content-center" v-else-if="items.length === 0">
              No items in this category 🥲
            </div>
            <itemCard
              v-for="item in items"
              :key="item.item_id"
              :title="item.item_name"
              @click="addToCart(item)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import itemCard from './ItemCard.vue'

export default {
  components: { itemCard },
  async mounted() {
    await this.$store.dispatch('foodData/getAllFoodCategories')

    if (this.filteredFoodData) {
      const firstItem = this.filteredFoodData[0].categoryID
      this.loadItems(firstItem), (this.selectedCategory = firstItem)
    }
  },

  data() {
    return {
      items: [],
      currentCartItems: [],
      selectedCategory: 0,
      billOnHold: [],
      loadingItems: true
    }
  },

  methods: {
    async loadItems(categoryID) {
      this.items = []
      const category = this.filteredFoodData.findIndex(
        (category) => category.categoryID === categoryID
      )
      this.loadingItems = true
      await this.$store.dispatch('foodData/getAllItems', categoryID)
      if ('detail' in this.filteredFoodData[category].items) {
        this.items = []
      } else {
        this.items = this.filteredFoodData[category].items
      }
      this.loadingItems = false
    },

    addToCart(item) {
      this.$store.commit('foodData/addItemTocurrentCart', item)
    }
  },

  computed: {
    filteredFoodData() {
      const foodCategories = this.$store.getters['foodData/allFoodCategories']
      return foodCategories
    }
  }
}
</script>
