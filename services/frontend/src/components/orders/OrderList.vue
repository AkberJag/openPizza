<template>
  <div class="card shadow d-flex">
    <!-- card header -->
    <div class="card-header">
      <div class="container">
        <div class="row">
          <div class="col-md-12 text-center fw-bold fs-4">
            <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
              <input
                type="radio"
                class="btn-check"
                name="btnradio"
                id="btnradio1"
                autocomplete="off"
                checked
              />
              <label class="btn btn-outline-secondary" for="btnradio1">New</label>

              <input
                type="radio"
                class="btn-check"
                name="btnradio"
                id="btnradio2"
                autocomplete="off"
              />
              <label class="btn btn-outline-secondary" for="btnradio2">Scheduled</label>

              <input
                type="radio"
                class="btn-check"
                name="btnradio"
                id="btnradio3"
                autocomplete="off"
              />
              <label class="btn btn-outline-secondary" for="btnradio3">In Progress</label>
              <input
                type="radio"
                class="btn-check"
                name="btnradio"
                id="btnradio4"
                autocomplete="off"
              />
              <label class="btn btn-outline-secondary" for="btnradio4">Complete</label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
