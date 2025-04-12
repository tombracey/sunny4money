// plane.js
window.onload = function() {
    // Check if it's the first page load
    if (!sessionStorage.getItem('pageLoaded')) {
        // If it's the first load, apply the animation
        const plane = document.querySelector('.plane');
        if (plane) {
            plane.style.animation = 'none'; // Reset the animation
            plane.offsetHeight; // Trigger reflow to reset the animation
            plane.style.animation = 'fly-plane 3s forwards'; // Reapply animation
        }

        // Set flag that the page has been loaded once
        sessionStorage.setItem('pageLoaded', 'true');
    }
};
