<template>
  <div class="card h-100 shadow-sm">
    <div class="card-header user-select-none">
      <div class="d-flex align-items-center">
        <div class="col-2"><i class="bi bi-search"></i></div>
        <div class="col-8 text-center fw-bold fs-4">Menu</div>
      </div>
    </div>
    <div class="card-body p-0 py-1" style="height: 0px">
      <div class="container-fluid h-100 overflow-hidden">
        <div class="row h-100">
          <div
            class="col border-end border-secondary border-2 py-2 h-100 overflow-auto"
            style="--bs-border-opacity: 0.3"
          >
            <!-- when no categories in the db, [] -->
            <div v-if="filteredFoodData.length == 0" class="text-center">
              <span class="fs-5 text-body-secondary">
                No categories available, add some first.
              </span>
            </div>

            <!-- Whan all categories fetched without any issues -->
            <div
              v-else-if="
                (filteredFoodData.length > 0) & !categoryLoadingStatus & (filteredFoodData != -1)
              "
            >
              <!-- menu categories (left) -->
              <MenuItem
                v-for="(category, index) in filteredFoodData"
                :key="category.categoryID"
                :title="category.categoryName"
                :selected="selectedCategory === category.categoryID"
                @click="loadItems(index), (selectedCategory = category.categoryID)"
              />
            </div>
            <!-- show loading spinner when fetching items -->
            <div v-else-if="categoryLoadingStatus" class="text-center">
              <Base-Spinner />
            </div>

            <!-- when something went worng with items -->
            <div v-else class="text-center">
              <span class="fs-5 text-body-secondary">Something went wrong</span> 😥
            </div>
          </div>
          <div class="col py-2 h-100 overflow-auto bg-secondary-subtle">
            <div class="text-center" v-if="items.length === 0 && loadingItems">
              <base-spinner></base-spinner>
            </div>
            <div class="text-center" v-else-if="items.length === 0">
              <span class="fs-5 text-body-secondary"> No items in this category</span> 🛒
            </div>

            <!-- items (right) -->
            <MenuItem
              v-for="(item, index) in items"
              :key="index"
              :title="item.name"
              :price="item.price"
              @click="addToCart(item, index)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MenuItem from './MenuItem.vue'

export default {
  components: { MenuItem },

  data() {
    return {
      items: [],
      selectedCategory: -1,
      loadingItems: false
    }
  },

  async mounted() {
    await this.$store.dispatch('foodMenu/getAllFoodCategories')

    if (this.filteredFoodData.length > 0) {
      this.loadItems(0), (this.selectedCategory = this.filteredFoodData[0].categoryID)
    }
  },

  methods: {
    async loadItems(categoryIDInArray) {
      this.loadingItems = true

      if (!this.filteredFoodData[categoryIDInArray].items) {
        let id = this.filteredFoodData[categoryIDInArray].categoryID
        await this.$store.dispatch('foodMenu/getAllItems', {
          itemID: id,
          itemArrayIndex: categoryIDInArray
        })
      }

      if (this.filteredFoodData[categoryIDInArray].items) {
        this.items = this.filteredFoodData[categoryIDInArray].items
      } else {
        this.items = []
      }

      this.loadingItems = false
    },

    addToCart(item, index) {
      this.$store.commit('orders/addItemToCurrentCart', [
        item,
        this.filteredFoodData[index].categoryName
      ])
    }
  },

  computed: {
    filteredFoodData() {
      return this.$store.getters['foodMenu/getAllFoodCategories']
    },
    categoryLoadingStatus() {
      return this.$store.getters['foodMenu/getCategoryLoadingStatus']
    }
  }
}
</script>
