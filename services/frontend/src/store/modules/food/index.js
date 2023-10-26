import actions from './actions'
import getters from './getters'
import mutations from './mutations'

export default {
  namespaced: true,
  state() {
    return {
      menuData: [
        // {
        // categoryID: 1,
        // categoryName: 'Fruits',
        // categoryImageURL: null,
        // items: [
        //   { itemID: 1, itemName: 'Apple', price: 0.75, calories: 95 },
        //   { itemID: 2, itemName: 'Banana', price: 0.6, calories: 105 }
        // ]
        // }
      ],
      // todo: later move this to the bill store
      cartsOnHold: [],
      currentCart: {
        id: null,
        customer: null,
        items: [],
        tax: 0,
        deliveryCharge: 0,
        extraCharge: 0,
        orderType: 'Dine In',
        subTotal: 0
      }
    }
  },
  actions,
  getters,
  mutations
}
