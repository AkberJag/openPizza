<template>
  <div class="h-100 p-3">
    <!-- Modal -->
    <div
      class="modal fade"
      id="staticBackdrop"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add {{ modelTitle }}</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div v-if="modelTitle === 'Category'">
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Category Name</label>
                <input type="text" class="form-control" v-model="newCategoryName" />
              </div>
            </div>
            <div v-else>
              <div class="mb-3">
                <label for="itemName" class="form-label">Item Name</label>
                <input id="itemName" type="text" class="form-control" v-model="newItemName" />
              </div>
              <div class="mb-3">
                <label for="itemPrice" class="form-label">Item Price</label>
                <input id="itemPrice" type="number" class="form-control" v-model="newItemPrice" />
              </div>
              <div class="mb-3">
                <label for="itemDescription" class="form-label">Item Description</label>
                <textarea
                  class="form-control"
                  placeholder="Enter Item Description here"
                  id="itemDescription"
                  style="height: 100px, margin: 150px;"
                  v-model="newItemDescription"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button
              v-if="modelTitle === 'Category'"
              type="button"
              class="btn btn-primary"
              @click="createCategory"
            >
              Create Category
            </button>
            <button v-else type="button" class="btn btn-primary" @click="createItem">
              Create Item
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="card h-100 shadow">
      <div class="container-fluid h-100">
        <div class="row h-100 py-2">
          <div class="col">
            <div class="card h-100 shadow-sm">
              <div class="card-body">
                <div
                  class="card text-center p-3 shadow-sm cursor-pointer mb-4"
                  v-for="(item, index) in allCategories"
                  :key="index"
                  @click="selectCategory({ index, item })"
                >
                  {{ item.categoryName }}
                </div>
              </div>
              <div
                class="card-footer text-center cursor-pointer"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
                @click="modelTitle = 'Category'"
              >
                Add Category
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card h-100 shadow-sm">
              <div class="card-body">
                <div class="card p-4 px-3 shadow-sm" v-for="(item, index) in items" :key="index">
                  <div class="d-flex">
                    <div class="fw-bold">{{ item.name }}</div>
                    <div class="ms-auto">${{ item.price }}</div>
                  </div>
                  {{ item.description }}
                </div>
              </div>
              <div
                class="card-footer text-center cursor-pointer"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
                @click="modelTitle = 'Item in category ' + currentCategoryName"
              >
                Add item in {{ currentCategoryName }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  async mounted() {
    await this.$store.dispatch('foodMenu/getAllFoodCategories')
  },

  data() {
    return {
      items: [],
      currentCategory: -1,
      currentCategoryName: '',
      modelTitle: 'Category',

      newCategoryName: '',

      newItemName: '',
      newItemPrice: 0,
      newItemDescription: ''
    }
  },
  methods: {
    async loadItems(categoryIDInArray) {
      if (!this.allCategories[categoryIDInArray].items) {
        let id = this.allCategories[categoryIDInArray].categoryID
        await this.$store.dispatch('foodMenu/getAllItems', {
          itemID: id,
          itemArrayIndex: categoryIDInArray
        })
      }

      if (this.allCategories[categoryIDInArray].items) {
        this.items = this.allCategories[categoryIDInArray].items
      } else {
        this.items = []
      }
    },

    async createCategory() {
      if (this.newCategoryName) {
        await this.$store.dispatch('adminItems/createCategory', {
          name: this.newCategoryName
        })
        await this.$store.dispatch('foodMenu/getAllFoodCategories')
      }
      this.newCategoryName = ''
    },

    async createItem() {
      if (this.currentCategory && this.newItemName && this.newItemPrice > 0) {
        await this.$store.dispatch('adminItems/createItem', {
          name: this.newItemName,
          price: this.newItemPrice,
          description: this.newItemDescription,
          category_id: this.currentCategory,
          category_name: this.currentCategoryName
        })
      }
      this.newCategoryName = ''
      this.newItemName = ''
      this.newItemPrice = 0
      this.newItemDescription = ''
    },

    selectCategory(payload) {
      this.loadItems(payload.index)
      this.currentCategory = payload.item.categoryID
      this.currentCategoryName = payload.item.categoryName
    }
  },

  computed: {
    allCategories() {
      return this.$store.getters['foodMenu/getAllFoodCategories']
    }
  }
}
</script>
