<template>
  <div class="h-100">
    <div class="card shadow d-flex">
      <div class="card-header">
        <div class="container">
          <div class="row">
            <div class="col-md-4 text-start p-1 text-body-secondary">
              <i class="bi bi-printer"> Print</i>
            </div>
            <div class="col-md-4 text-center fw-bold fs-4">#9</div>
            <div class="col-md-4 text-end p-1">
              <div class="d-inline mx-3 text-body-secondary"><i class="bi bi-copy"></i> Copy</div>
              <div class="d-inline text-body-secondary"><i class="bi bi-trash"></i> Clear</div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body p-1" style="overflow: hidden; height: calc(100vh - 73px)">
        <div class="container">
          <div class="row row-cols-1 h-100">
            <!-- address -->
            <div class="col mt-2">
              <div class="card shadow-sm" style="overflow: auto; height: calc((100vh - 180px) / 3)">
                <div class="card-body p-2 ms-2" style="overflow: auto">
                  <span class="badge text-bg-secondary float-end me-2">DELIVERY</span>
                  <p class="m-0"><strong>Bill Gates</strong></p>
                  <p class="mb-0 text-body-secondary">(555) 555-6666</p>
                  <p class="mb-0 text-body-secondary">123 Main Street</p>
                  <p class="mb-0 text-body-secondary">Belfast MA, 94122</p>
                </div>
                <div class="card-footer bg-transparent pt-1 pb-1">
                  <div class="d-grid gap-2 d-md-flex">
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-stickies mx-2"></i> Order Note
                    </button>
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-patch-check mx-2"></i>Discount
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- items -->
            <div class="col mt-2">
              <div class="card shadow-sm">
                <div class="card-body" style="overflow: auto; height: calc((100vh - 120px) / 3)">
                  <table class="table table-hover">
                    <tbody>
                      <tr>
                        <th scope="row" class="fs-6">1</th>
                        <td>
                          <div class="row me-0">
                            <div
                              class="aa fw-bold text-capitalize fs-6 col-10 m-0"
                              data-bs-toggle="collapse"
                              href="#collapseExample"
                              aria-expanded="false"
                              style="cursor: pointer"
                            >
                              chicken francese
                              <span class="right-icon ms-auto">
                                <i class="bi bi-chevron-down"></i>
                              </span>
                            </div>
                            <div class="fw-bold text-end col-2">$12</div>
                          </div>
                          <div class="collapse m-0" id="collapseExample">
                            <div class="row me-0">
                              <div class="col-10">
                                <span class="me-2 text-danger" style="opacity: 75%">Type</span>
                                <span class="text-body-secondary">Dinner</span>
                              </div>
                              <div class="col-2 text-end text-body-secondary">$12</div>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="card-footer bg-transparent pt-1 pb-1">
                  <div class="d-grid gap-2 d-md-flex">
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-pencil mx-2"></i>Modify
                    </button>
                    <button type="button" class="btn btn-outline-secondary col-6">
                      <i class="bi bi-sticky mx-2"></i> Add Note
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <!-- amount -->
            <div class="col mt-2 mb-5" style="overflow: auto; height: calc((100vh - 220px) / 3)">
              <div class="list-group h-100 shadow-sm">
                <div
                  class="shadow-sm list-group-item list-group-item-action d-flex justify-content-between"
                >
                  <div class="text-success ms-2">+ Add delivery charge</div>
                  <div class="text-success me-2">+ Add extra charge</div>
                </div>
                <div
                  class="list-group-item list-group-item-action d-flex justify-content-between list-group-item-secondary p-1 px-3"
                >
                  <div class="text-dark-emphasis ms-2">Subtotal</div>
                  <div class="text-dark-emphasis me-2 pe-2">$16.00</div>
                </div>
                <div
                  class="list-group-item list-group-item-action d-flex justify-content-between list-group-item-secondary p-1 px-3"
                >
                  <div class="text-dark-emphasis ms-2 me-3" for="flexSwitchCheckChecked">Tax</div>
                  <div class="form-check form-switch me-auto mt-1">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      role="switch"
                      id="flexSwitchCheckChecked"
                      checked
                    />
                  </div>

                  <div class="text-dark-emphasis me-2 pe-2">$1.42</div>
                </div>
                <div class="list-group-item d-flex justify-content-between d-grid gap-2 shadow-sm">
                  <button type="button" class="btn btn-secondary col-4">Hold</button>
                  <button type="button" class="btn btn-danger col-8">Pay</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
li {
  padding-left: 2em;
  margin-bottom: 1em;
}
.right-icon {
  display: inline-flex;
  transition: all 0.3s;
  opacity: 50%;
}

.aa[aria-expanded='true'] .right-icon {
  transform: rotate(180deg);
}
</style>
