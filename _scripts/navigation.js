{
  const initializeNavigation = () => {
    const header = document.querySelector(".site-header");

    if (!header) return;

    const mobileBreakpoint = window.matchMedia("(max-width: 1100px)");
    const navToggle = header.querySelector(".nav-toggle");
    const navigation = header.querySelector(".site-nav");
    const dropdowns = Array.from(
      header.querySelectorAll(".site-nav__item--dropdown"),
    );

    const closeDropdown = (dropdown) => {
      dropdown.classList.remove("is-open");
      dropdown.querySelector(".dropdown-toggle").setAttribute("aria-expanded", "false");
    };

    const closeDropdowns = (exception) => {
      dropdowns.forEach((dropdown) => {
        if (dropdown !== exception) closeDropdown(dropdown);
      });
    };

    const closeNavigation = () => {
      navigation.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Open navigation menu");
      closeDropdowns();
    };

    navToggle.addEventListener("click", () => {
      const isOpen = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "Open navigation menu" : "Close navigation menu");
      navigation.classList.toggle("is-open", !isOpen);
      if (isOpen) closeDropdowns();
    });

    dropdowns.forEach((dropdown) => {
      const toggle = dropdown.querySelector(".dropdown-toggle");

      dropdown.addEventListener("mouseenter", () => {
        if (mobileBreakpoint.matches) return;
        closeDropdowns(dropdown);
        dropdown.classList.add("is-open");
        toggle.setAttribute("aria-expanded", "true");
      });

      dropdown.addEventListener("mouseleave", () => {
        if (!mobileBreakpoint.matches) closeDropdown(dropdown);
      });

      toggle.addEventListener("click", (event) => {
        const isOpen = toggle.getAttribute("aria-expanded") === "true";
        if (!mobileBreakpoint.matches && event.detail > 0 && isOpen) return;
        closeDropdowns(dropdown);
        dropdown.classList.toggle("is-open", !isOpen);
        toggle.setAttribute("aria-expanded", String(!isOpen));
      });
    });

    document.addEventListener("click", (event) => {
      if (!header.contains(event.target)) {
        closeDropdowns();
        if (mobileBreakpoint.matches) closeNavigation();
      }
    });

    header.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") return;

      const openDropdown = header.querySelector(".site-nav__item--dropdown.is-open");

      if (openDropdown) {
        const toggle = openDropdown.querySelector(".dropdown-toggle");
        closeDropdown(openDropdown);
        toggle.focus();
      } else if (navigation.classList.contains("is-open")) {
        closeNavigation();
        navToggle.focus();
      }
    });

    mobileBreakpoint.addEventListener("change", closeNavigation);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeNavigation);
  } else {
    initializeNavigation();
  }
}
