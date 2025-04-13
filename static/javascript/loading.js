document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('sunnyForm');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        results.innerHTML = '';
        loading.classList.add('fade-in');
        loading.style.display = 'block';

        const formData = new FormData(form);

        try {
            const response = await fetch('', {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            });

            if (!response.ok) throw new Error('Network response was not ok');

            const data = await response.json();

            loading.classList.remove('fade-in');
            loading.style.display = 'none';

            results.innerHTML = data.html;

            document.querySelectorAll('.container').forEach((el, i) => {
                el.offsetHeight;
                setTimeout(() => {
                    el.classList.add('visible');
                }, i * 200);
            });

        } catch (error) {
            console.error('Fetch error:', error);
            loading.classList.remove('fade-in');
            loading.style.display = 'none';
            results.innerHTML = '<h2>Something went wrong. Please try again later.</h2>';
        }
    });
});
