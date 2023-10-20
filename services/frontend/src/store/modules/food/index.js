import actions from './actions'
import getters from './getters'
import mutations from './mutations'

export default {
  namespaced: true,
  state() {
    return {
      menuData: [
        {
          // categoryID: 1,
          // categoryName: 'Fruits',
          // categoryImageURL: null,
          // items: [
          //   { itemID: 1, itemName: 'Apple', price: 0.75, calories: 95 },
          //   { itemID: 2, itemName: 'Banana', price: 0.6, calories: 105 }
          // ]
        }
      ]
    }
  },
  actions,
  getters,
  mutations
}
