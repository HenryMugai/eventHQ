document.addEventListener('DOMContentLoaded', () => {

    const menuToggle =
        document.getElementById('menuToggle');

    const navLinks =
        document.getElementById('navLinks');

    if (menuToggle) {

        menuToggle.addEventListener('click', () => {

            navLinks.classList.toggle('active');
        });
    }

    // Auto-hide alerts

    const alerts =
        document.querySelectorAll('.alert');

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
});