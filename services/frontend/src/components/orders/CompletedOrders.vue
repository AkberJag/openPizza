<template>
  <div class="col">
    <div class="d-flex flex-column flex-shrink-0 container-fluid">
      <div class="row overflow-auto" style="max-height: 300px">
        <div class="col">
          <table class="table">
            <thead class="sticky-top" style="font-size: 0.8em">
              <tr>
                <th scope="col" style="max-width: 55px">Order Number</th>
                <th scope="col">Type</th>
                <th scope="col">Created at</th>
                <th scope="col">Order Notes</th>
                <th scope="col">Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(order, index) in totalOrders" :key="index">
                <th>{{ order.id }}</th>
                <td>{{ order.order_type }}</td>
                <td>
                  {{
                    new Date(order.created_at).toLocaleString('en-US', {
                      hour12: true,
                      hour: 'numeric',
                      minute: 'numeric',
                      month: 'long',
                      day: 'numeric',
                      year: 'numeric'
                    })
                  }}
                </td>
                <td>{{ order.order_notes }}</td>
                <td>${{ order.order_total.toFixed(2) }}</td>
                <!-- <td>{{ order }}</td> -->
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="row w-100">
        <div class="col">
          <div class="d-flex" style="height: 450px">
            <div
              class="w-100 d-flex align-items-center justify-content-center"
              style="width: 100% !important"
            >
              <canvas id="orderPriceGraph"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
  async mounted() {
    this.totalOrders = await this.$store.dispatch('orders/loadAllOrders')

    let ctx = document.getElementById('orderPriceGraph')

    if (this.totalOrders) {
      new Chart(document.getElementById('orderPriceGraph'), {
        type: 'line',
        data: {
          labels: this.totalOrders.map((order) =>
            new Date(order.created_at).toLocaleString('en-US', {
              hour12: true,
              hour: 'numeric',
              minute: 'numeric',
              month: 'short',
              day: 'numeric',
              year: 'numeric'
            })
          ),
          datasets: [
            {
              label: 'Price',
              data: this.totalOrders.map((order) => order.order_total),
              borderColor: 'rgb(75, 192, 192)',
              responsive: true,
              maintainAspectRatio: false
            }
          ]
        },
        options: {
          scales: {
            y: {
              min: 0
            }
          }
        }
      })
    }
  },
  data() {
    return {
      totalOrders: ''
    }
  }
}
</script>
