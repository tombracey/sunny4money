document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("sunnyForm");
    const loading = document.getElementById("loading");
    const results = document.getElementById("results");

    if (form) {
        form.addEventListener("submit", function () {
            if (results) {
                results.classList.add("fade-out");
            }

            const containers = document.querySelectorAll(".container");
            containers.forEach(container => {
                container.classList.remove("visible");
            });

            setTimeout(() => {
                loading.style.display = "block";
            }, 300);
        });
    }

    const containers = document.querySelectorAll(".container");
    if (containers.length > 0) {
        containers.forEach((container, i) => {
            setTimeout(() => {
                container.classList.add("visible");
            }, 300 + i * 100);
        });

        if (loading) {
            loading.classList.add("fade-out");
            setTimeout(() => {
                loading.style.display = "none";
                loading.classList.remove("fade-out");
            }, 500);
        }

        if (results) {
            results.classList.remove("fade-out");
        }
    }
});
