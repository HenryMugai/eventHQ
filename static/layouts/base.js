document.addEventListener('DOMContentLoaded', () => {

    // ==========================================
    // Mobile Menu
    // ==========================================

    const menuToggle =
        document.getElementById(
            'menuToggle'
        );

    const navLinks =
        document.getElementById(
            'navLinks'
        );

    if (menuToggle && navLinks) {

        menuToggle.addEventListener(
            'click',
            () => {

                navLinks.classList.toggle(
                    'active'
                );
            }
        );

        document.addEventListener(
            'click',
            (event) => {

                const clickedInsideMenu =
                    navLinks.contains(
                        event.target
                    );

                const clickedToggle =
                    menuToggle.contains(
                        event.target
                    );

                if (
                    !clickedInsideMenu &&
                    !clickedToggle
                ) {

                    navLinks.classList.remove(
                        'active'
                    );
                }
            }
        );
    }

    // ==========================================
    // Auto Hide Alerts
    // ==========================================

    const alerts =
        document.querySelectorAll(
            '.alert'
        );

    alerts.forEach(alert => {

        setTimeout(() => {

            alert.style.opacity = '0';

            alert.style.transform =
                'translateY(-10px)';

            setTimeout(() => {

                alert.remove();

            }, 300);

        }, 5000);
    });

    // ==========================================
    // Navbar Shadow On Scroll
    // ==========================================

    const header =
        document.querySelector(
            '.site-header'
        );

    window.addEventListener(
        'scroll',
        () => {

            if (
                window.scrollY > 30
            ) {

                header.style.boxShadow =
                    '0 12px 40px rgba(0,0,0,.08)';

            } else {

                header.style.boxShadow =
                    '0 5px 25px rgba(0,0,0,.04)';
            }
        }
    );

    // ==========================================
    // Reveal Animations
    // ==========================================

    const revealElements =
        document.querySelectorAll(
            '.reveal'
        );

    const observer =
        new IntersectionObserver(

            entries => {

                entries.forEach(
                    entry => {

                        if (
                            entry.isIntersecting
                        ) {

                            entry.target.classList.add(
                                'revealed'
                            );
                        }
                    }
                );

            },

            {
                threshold: 0.15
            }
        );

    revealElements.forEach(
        element => {

            observer.observe(
                element
            );
        }
    );

});