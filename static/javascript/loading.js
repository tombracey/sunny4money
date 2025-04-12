document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("sunnyForm");
    const loading = document.getElementById("loading");
    const results = document.getElementById("results");

    if (form) {
        form.addEventListener("submit", function () {
            // Fade out existing results
            if (results) {
                results.classList.add("fade-out");
            }
                

            // Hide containers
            const containers = document.querySelectorAll(".container");
            containers.forEach(container => {
                container.classList.remove("visible");
            });

            // Wait for fade-out to finish before showing loader
            setTimeout(() => {
                loading.style.display = "block";
            }, 300);
        });
    }

    // On page load with results, show them with animation
    const containers = document.querySelectorAll(".container");
    if (containers.length > 0) {
        containers.forEach(container => {
            setTimeout(() => {
                container.classList.add("visible");
            }, 300); // Wait a moment so it looks smooth
        });

        // Hide loading with fade-out
        if (loading) {
            loading.classList.add("fade-out");
            setTimeout(() => {
                loading.style.display = "none";
                loading.classList.remove("fade-out");
            }, 500);
        }

        // Remove fade-out from results so it doesn't persist
        results.classList.remove("fade-out");
    }
});