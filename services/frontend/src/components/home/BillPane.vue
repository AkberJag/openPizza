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
              <div class="card shadow-sm" style="overflow: auto; height: calc((100vh - 120px) / 3)">
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
                      Order Note
                    </button>
                    <button type="button" class="btn btn-outline-secondary col-6">Discount</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- items -->
            <div class="col mt-2">
              <div class="card shadow-sm">
                <div
                  class="card-body"
                  style="overflow: auto; height: calc((100vh - 120px) / 3)"
                ></div>
              </div>
            </div>

            <!-- amount -->
            <div class="col mt-2 mb-2">
              <div class="card shadow-sm">
                <div
                  class="card-body"
                  style="overflow: auto; height: calc((100vh - 120px) / 3)"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
