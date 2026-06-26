/* ==========================================
   EventHQ Admin Layout
   admin_base.js
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.querySelector(".sidebar");
    const menuToggle = document.getElementById("menu-toggle");

    // ==========================
    // Mobile Sidebar Toggle
    // ==========================
    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            sidebar.classList.toggle("active");
        });
    }

    // ==========================
    // Close Sidebar on Mobile
    // ==========================
    document.addEventListener("click", (e) => {

        if (
            window.innerWidth <= 991 &&
            sidebar &&
            !sidebar.contains(e.target) &&
            menuToggle &&
            !menuToggle.contains(e.target)
        ) {
            sidebar.classList.remove("active");
        }

    });

    // ==========================
    // Active Navigation
    // ==========================
    const currentPath = window.location.pathname;

    document.querySelectorAll(".sidebar nav a").forEach(link => {

        const href = link.getAttribute("href");

        if (href && currentPath === href) {
            link.classList.add("active");
        }

    });

    // ==========================
    // Flash Messages
    // ==========================
    const flashes = document.querySelectorAll(".flash");

    flashes.forEach(flash => {

        setTimeout(() => {

            flash.style.transition = "0.4s";
            flash.style.opacity = "0";
            flash.style.transform = "translateY(-10px)";

            setTimeout(() => {
                flash.remove();
            }, 400);

        }, 5000);

    });

});