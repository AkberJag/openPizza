<template>
  <div class="d-flex flex-column flex-shrink-0 bg-light min-vh-100" style="width: 4.5rem">
    <div class="text-center" style="font-size: xxx-large">🍕</div>
    <ul class="nav nav-pills nav-flush flex-column mb-auto text-center flex-fill">
      <!-- menus -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom border-top"
          aria-current="page"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Home"
        >
          <i class="bi bi-pencil-square"></i>
        </a>
      </li>
      <!-- orders -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Dashboard"
        >
          <i class="bi bi-journals"></i>
        </a>
      </li>
      <!-- Customers -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Orders"
        >
          <i class="bi bi-people"></i>
        </a>
      </li>
      <!-- Cash Management -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Products"
        >
          <i class="bi bi-cash-stack"></i>
        </a>
      </li>
      <!-- Delivery Management (Optional Feature) -->
      <li>
        <a
          href="#"
          class="nav-link py-3 border-bottom"
          title=""
          data-bs-toggle="tooltip"
          data-bs-placement="right"
          data-bs-original-title="Customers"
        >
          <i class="bi bi-truck"></i>
        </a>
      </li>
    </ul>

    <!-- Settings -->
    <div class="dropdown border-top">
      <a
        href="#"
        class="d-flex align-items-center justify-content-center p-3 link-dark text-decoration-none dropdown-toggle"
        id="dropdownUser3"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <i class="bi bi-person-circle"></i>
      </a>
      <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser3">
        <li><a class="dropdown-item" href="#">New project...</a></li>
        <li><a class="dropdown-item" href="#">Settings</a></li>
        <li><a class="dropdown-item" href="#">Profile</a></li>
        <li><hr class="dropdown-divider" /></li>
        <li><a class="dropdown-item" href="#">Sign out</a></li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.nav-link {
  border-radius: 0;
}

.bi {
  font-size: 1.5rem;
}
</style>
